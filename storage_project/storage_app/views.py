from django.db.models import F, ExpressionWrapper, DecimalField, Sum
from rest_framework.response import Response
from rest_framework.decorators import api_view

from storage_app.models import Item, Category
from storage_app.serializers import ItemSerializer


def calculate_total_volume():
    items = Item.objects.all().filter(is_active=True)

    total_volume = items.annotate(
        item_volume=ExpressionWrapper(
            F('package_length') * F('package_width') * F('package_height'),
            output_field=DecimalField(max_digits=10, decimal_places=2)
        )
    ).aggregate(total_volume=Sum('item_volume'))['total_volume'] or 0

    return total_volume


@api_view(['GET'])
def get_storage(request):
    total_volume = calculate_total_volume()
    categories = Category.objects.prefetch_related('item_set').all()

    serialized_categories = []
    for category in categories:
        serialized_items = ItemSerializer(category.item_set.all(), many=True).data
        category_data = {
            'id': category.id,
            'name_ru': category.name_ru,
            'name_en': category.name_en,
            'category_code': category.category_code,
            'items': serialized_items
        }
        serialized_categories.append(category_data)

    storage_data = {
        'items_volume': str(total_volume),
        'categories': serialized_categories,
    }

    return Response(storage_data)


