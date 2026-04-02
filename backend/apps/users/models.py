from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinLengthValidator


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
