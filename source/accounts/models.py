from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE,  verbose_name="User", related_name="profile")

    def __str__(self):
        return self.user.get_full_name() + "'s Profile"

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
