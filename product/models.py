from django.db import models
from django.utils.timezone import now
from multiselectfield import MultiSelectField


class Product(models.Model):
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'
    X = 'X'

    SIZE_CHOICES = (
        (X+SMALL, X+SMALL),
        (SMALL, SMALL),
        (MEDIUM, MEDIUM),
        (LARGE, LARGE),
        (X+LARGE, X+LARGE),
        (X+X+LARGE, X+X+LARGE),
    )

    TYPE_CHOICES = (
        ('men', 'Men'),
        ('women', 'Women'),
        ('children', 'Children')
    )

    def name_file(self, filename):
        return '/'.join(['images', str(self.title), filename])

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)
    available_sizes = MultiSelectField(choices=SIZE_CHOICES, max_choices=10, min_choices=1, null=False, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    picture = models.ImageField(upload_to=name_file, blank=False, null=False)
    client_type = MultiSelectField(choices=TYPE_CHOICES, max_choices=10, min_choices=1, null=False, blank=False)
    product_specification = models.ForeignKey('ProductSpecifications', on_delete=models.CASCADE, null=False, blank=False)

    rate = models.DecimalField(null=False, blank=False, max_digits=2, decimal_places=1)
    created_at = models.DateTimeField(auto_created=True, default=now, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


class ProductSpecifications(models.Model):
    TYPE_CHOICES = (
        ('men', 'Men'),
        ('women', 'Women'),
        ('children', 'Children')
    )
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255, choices=TYPE_CHOICES)
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category

