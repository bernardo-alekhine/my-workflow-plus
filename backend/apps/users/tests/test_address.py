import pytest
from .factories import UserFactory, AddressFactory


@pytest.mark.django_db
class TestAddress:
    def test_set_default(self):
        """Tests for setting address as default (boolean). When one address set to True, all OTHERS are set to False."""
        user = UserFactory()
        address_1 = AddressFactory(user=user)
        address_2 = AddressFactory(user=user, is_default=True)

        address_1.set_as_default()
        address_2.refresh_from_db()

        assert address_1.is_default is True
        assert address_2.is_default is False

    def test_address_str(self):
        """Test for expected string format when using __str__."""
        address = AddressFactory()
        assert str(address) == f"{address.street}, {address.number}, {address.city}, {address.state}, {address.country}"
