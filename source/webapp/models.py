from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    category_choices = [('other', 'Other'), ('dairy', 'Dairy'), ('soft_drinks', 'Soft Drinks'),
                        ('groceries', 'Groceries')]
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Name")
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name="Description")
    category = models.CharField(max_length=100, choices=category_choices, default='1')
    picture = models.ImageField(upload_to="avatars", null=True, blank=True, verbose_name="Avatar")

    def __str__(self):
        return f'{self.id} {self.name}'

    def get_absolute_url(self):
        return reverse("webapp:product_view", kwargs={"pk": self.pk})

    class Meta:
        db_table = "products"
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Review(models.Model):
    author = models.ForeignKey(get_user_model(),
                               on_delete=models.CASCADE,
                               verbose_name="Author",
                               related_name="Review")
    product = models.ForeignKey("webapp.Product",  on_delete=models.CASCADE, related_name='product')
    review_text = models.TextField(max_length=1000, null=False, blank=False, verbose_name="Review text")
    rating = models.PositiveIntegerField(default=1,
                                         validators=[MaxValueValidator(5), MinValueValidator(1)],
                                         null=False, blank=False)
    is_moderated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date created")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date updated")

    def __str__(self):
        return f'{self.id} {self.author} - {self.review_text}'

    # def get_absolute_url(self):
    #     return reverse("webapp:product_view", kwargs={"pk": self.pk})

    class Meta:
        db_table = "reviews"
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
