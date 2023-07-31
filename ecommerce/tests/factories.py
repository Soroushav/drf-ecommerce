import factory

from apps.product.models import Category, Brand, Product

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: "Cat_%d" % n)

class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = factory.Sequence(lambda n: "Brand_%d" % n)

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Sequence(lambda n: "Product_%d" % n)
    description = factory.Sequence(lambda n: "Description_%d" % n)
    type = factory.Sequence(lambda n: "Type_%d" % n)
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)