import factory
from apps.users.models import User, TaxRegistration


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")


class TaxRegistrationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TaxRegistration

    user = factory.SubFactory(UserFactory)
    country_code = "BR"
    id_type = "CNPJ"
    value = factory.Sequence(lambda n: f"123456780001{n:02d}")
