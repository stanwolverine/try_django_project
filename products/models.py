from django.db import models
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10000, decimal_places=2)
    mrp = models.DecimalField(max_digits=10000, decimal_places=2)
    summary = models.TextField()
    featured = models.BooleanField()

    # def get_absolute_url(self):
    #     # 1st way
    #     # return f'/products/{self.id}' # in this case products keyword is static
    #     # 2nd way
    #     return reverse('app_name:<url-name>', kwargs={'id': self.id})
