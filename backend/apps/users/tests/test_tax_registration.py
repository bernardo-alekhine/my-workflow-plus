from django.db import IntegrityError
import pytest
from .factories import UserFactory, TaxRegistrationFactory


@pytest.mark.django_db
class TestTaxRegistration:
    def test_user_tax_ids_relationship(self):
        """Test user has related attribute of tax_ids declared in tax registration, correct values and count."""
        user = UserFactory()
        cpf_tax_registration = TaxRegistrationFactory(user=user, id_type="CPF")
        assert user.tax_ids.get(id=cpf_tax_registration.id).id_type == "CPF"
        assert cpf_tax_registration.user == user

    def test_user_can_have_multiple_tax_ids(self):
        """Test that a user can have multiple tax ids"""
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

    def test_tax_registration_str(self):
        """Test for expected string format when using __str__."""
        tax_id = TaxRegistrationFactory(country_code="US", id_type="EIN", value="12-34567")
        assert str(tax_id) == "EIN: 12-34567 (US)"
