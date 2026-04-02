import pytest
from django.db import DataError, IntegrityError
from .factories import UserFactory


@pytest.mark.django_db
class TestUsers:
    def test_occupation_length_boundary(self):
        # Success at exactly 50
        UserFactory(occupation="A" * 50)

        # Failure at 51 (Database level)
        with pytest.raises((IntegrityError, DataError)):
            UserFactory(occupation="A" * 51)
