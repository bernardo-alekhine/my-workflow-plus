from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinLengthValidator
from apps.core.models import BaseModel


# Create your models here.
class User(AbstractUser):
    occupation = models.CharField(max_length=50, null=True, blank=True)


class TaxRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tax_ids")
    country_code = models.CharField(max_length=2, db_index=True)

    # The Type (e.g., "CNPJ", "CPF", "VAT", "EIN")
    id_type = models.CharField(max_length=20)

    # The actual tax id value
    value = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(5)],
        help_text="Store raw alphanumeric values only.",
        db_index=True,
    )

    class Meta:
        # Prevents assigning the same ID twice for the same type in a country
        unique_together = ("country_code", "id_type", "value")

    def __str__(self):
        return f"{self.id_type}: {self.value} ({self.country_code})"


class Address(BaseModel):
    class Types(models.TextChoices):
        HOUSE = "house", "House"
        APT = "apt", "Apartment"
        OFFICE = "off", "Office"

    address_type = models.CharField(max_length=20, choices=Types.choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="addresses")
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    neighborhood = models.CharField(max_length=100, blank=True)
    line_2 = models.CharField(max_length=100, null=True, blank=True, help_text="Apartment, suite, unit, floor, etc.")
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    complement = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=20)
    is_default = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Addresses"

    def set_as_default(self):
        """Only one user's address can be default. When one address set to True, all OTHERS are set to False."""
        Address.objects.filter(user=self.user).update(is_default=False)
        self.is_default = True
        self.save()

        def __str__(self):
            return f"{self.street}, {self.number}, {self.city}, {self.state}, {self.country}"
