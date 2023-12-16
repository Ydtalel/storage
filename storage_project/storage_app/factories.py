from factory import Faker, SubFactory
from factory.django import DjangoModelFactory
from storage_app.models import Category, Item

class UniqueNameRuFaker(Faker):
    def __init__(self, **kwargs):
        super().__init__("word", **kwargs)

    def generate(self, create, params):
        name = super().generate(create, params)
        while Category.objects.filter(name_ru=name).exists():
            name = super().generate(create, params)
        return name

class CategoryFactory(DjangoModelFactory):
    name_ru = UniqueNameRuFaker()
    name_en = Faker('word')
    category_code = Faker('random_int', min=1, max=1000)

    class Meta:
        model = Category

class ItemFactory(DjangoModelFactory):
    category = SubFactory(CategoryFactory)
    code = Faker('random_int', min=1, max=1000000)
    internal_code = Faker('random_int', min=1, max=1000)
    package_length = Faker('random_number', digits=2)
    package_width = Faker('random_number', digits=2)
    package_height = Faker('random_number', digits=2)
    name_ru = UniqueNameRuFaker()
    description_ru = Faker('text')
    description_en = Faker('text')
    amount = Faker('random_int', min=1, max=100)
    cost = Faker('random_number', digits=2)
    is_active = Faker('boolean', chance_of_getting_true=70)

    class Meta:
        model = Item
