from django.db import models

class MenuItem(models.Model):
    TYPE_CHOICES = (
        ('APPETIZER', 'Appetizer'),
        ('MAIN', 'Main Course'),
        ('DESSERT', 'Dessert'),
        ('DRINK', 'Drink'),
    )

    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='MAIN')

    def __str__(self):
        return self.name