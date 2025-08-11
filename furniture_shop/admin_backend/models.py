from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return (f"{self.name}")


class Product(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    color = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"

class ProductImage(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images')


    def __str__(self):
        return f"{self.product.name} - {self.image}"