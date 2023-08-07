import factory

from apps.product.models import Category, Brand, Product
from apps.user.models import RegularUser, GoldenUser

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: "Cat_%d" % n)

class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = factory.Sequence(lambda n: "Brand_%d" % n)
    category = factory.SubFactory(CategoryFactory)

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Sequence(lambda n: "Product_%d" % n)
    description = factory.Sequence(lambda n: "Description_%d" % n)
    type = factory.Sequence(lambda n: "Type_%d" % n)
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)


class RegularFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RegularUser

    username = factory.Sequence(lambda n: "r_username_%d" % n)
    password = factory.Sequence(lambda n: "r_password_%d" % n)
    email = factory.Sequence(lambda n: "r_email_%d@gmail.com" % n)

class GoldenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GoldenUser

    username = factory.Sequence(lambda n: "g_username_%d" % n)
    password = factory.Sequence(lambda n: "g_password_%d" % n)
    email = factory.Sequence(lambda n: "g_email_%d@gmail.com" % n)