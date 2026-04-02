import factory
from apps.users.models import User, TaxRegistration, Address


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker("user_name")

    class Meta:
        model = User


class TaxRegistrationFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    country_code = "BR"
    id_type = "CNPJ"
    value = factory.Sequence(lambda n: f"123456780001{n:02d}")

    class Meta:
        model = TaxRegistration


class AddressFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    address_type = factory.Iterator([choice[0] for choice in Address.Types.choices])
    street = factory.Faker("street_address")
    number = factory.Faker("building_number")
    neighborhood = factory.Faker("street_name", locale="pt_BR")
    line_2 = factory.Faker("secondary_address")
    city = factory.Faker("city")
    state = factory.Faker("state_abbr")
    country = factory.Faker("country")
    complement = factory.Faker("secondary_address")
    postal_code = factory.Faker("postalcode")
    is_default: bool = False

    class Meta:
        model = Address
