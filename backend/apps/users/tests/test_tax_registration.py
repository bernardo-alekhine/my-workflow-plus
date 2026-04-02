from django.db import IntegrityError
import pytest
from .factories import UserFactory, TaxRegistrationFactory


@pytest.mark.django_db
class TestTaxRegistration:
    def test_user_can_have_multiple_tax_ids(self):
        """ "Test that a user can have multiple tax ids"""
        user = UserFactory()
        TaxRegistrationFactory(user=user, id_type="CPF", value="11122233344")
        TaxRegistrationFactory(user=user, id_type="CNPJ", value="11222333000199")
        assert user.tax_ids.count() == 2

    def test_duplicate_tax_id_fails(self):
        """Test the unique_together constraint"""
        TaxRegistrationFactory(country_code="US", id_type="EIN", value="12-34567")

        with pytest.raises(IntegrityError):
            # Try to create the exact same record again
            TaxRegistrationFactory(country_code="US", id_type="EIN", value="12-34567")
