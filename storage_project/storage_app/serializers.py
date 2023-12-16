import hashlib

from rest_framework import serializers

from .models import Category, Item


class AdditionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['info']


class ItemSerializer(serializers.ModelSerializer):
    hash = serializers.SerializerMethodField()
    additional = AdditionalInfoSerializer(many=True)

    class Meta:
        model = Item
        fields = ['id', 'hash', 'internal_code', 'name_ru', 'description_ru', 'description_en', 'cost', 'additional']

    def get_hash(self, obj):
        item_id_str = str(obj.id)
        hasher = hashlib.sha256()
        hasher.update(item_id_str.encode('utf-8'))
        return hasher.hexdigest()

    # https://ilyachch.gitbook.io/django-rest-framework-russian-documentation/overview/navigaciya-po-api/serializers#pereopredelenie-povedeniya-serializacii-i-deserializacii
    def to_representation(self, instance):
        data = super().to_representation(instance)
        additional_info = instance.additional.all()
        data['hash'] = self.get_hash(instance)
        data['additional'] = AdditionalInfoSerializer(additional_info, many=True).data
        return data


class CategorySerializer(serializers.ModelSerializer):
    items = ItemSerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = ['id', 'name_ru', 'name_en', 'category_code', 'items']


class StorageSerializer(serializers.Serializer):
    items_volume = serializers.DecimalField(max_digits=10, decimal_places=2)
    categories = CategorySerializer(many=True, read_only=True)
