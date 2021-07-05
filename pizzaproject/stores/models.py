from django.db import models
from django.core.validators import RegexValidator


class Pizzeria(models.Model):
    pizzeria_name = models.CharField(max_length=200, blank=False)
    street = models.CharField(max_length=400, blank=True)
    city = models.CharField(max_length=400, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    zip_code = models.IntegerField(blank=True, default=0)
    website = models.URLField(max_length=420, blank=True)
    phone_number = models.CharField(
        validators=[RegexValidator(regex=r'\+375\d{9}')],
        max_length=13,
        blank=True,
        default="+375"
    )
    description = models.TextField(blank=True)
    logo_image = models.ImageField(
        upload_to='pizzaiaImages',
        blank=True,
        default="pizzariaImages/pizzalogo.png"
    )

    def __str__(self):
        return f"{self.pizzeria_name}, {self.city}"
