from django.db import models
from applications.users.models.users import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from applications.reference_data.models.countries import Country
from applications.reference_data.enums.salary_range import SalaryRange
from applications.abstracts.models.global_abastract_model import AbstractModel

# Create your models here.


class UserProfile(AbstractModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone = models.CharField(max_length=15, null=True, blank=True)
    institution = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state_province = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="country_profile",
        blank=True,
        null=True,
    )
    phone = models.CharField(max_length=18, null=True, blank=True)
    profile_avatar_url = models.URLField(blank=True, null=True)
    salary_range = models.CharField(
        max_length=30, choices=SalaryRange.choices, null=True, blank=True
    )

    class Meta:
        db_table = "users_profile"
        verbose_name = "User Profile"
        verbose_name_plural = "Users Profiles"

    def __str__(self):
        return f"Perfil de {self.user.username}"
