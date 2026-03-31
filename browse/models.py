from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Product Model - Selling clothing items
#       description:    short title/name of the product
#       comment:        notes about the product
#       price:          price of the product
#       category:       foreign key to Category (each product belongs to one category)
#       tags:           many-to-many relationship with Tag (a product can have multiple tags)
#       created_at:     when the product was created
class Product(models.Model):
    description = models.CharField(max_length=100)
    comment = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    tags = models.ManyToManyField(Tag, related_name="products", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
