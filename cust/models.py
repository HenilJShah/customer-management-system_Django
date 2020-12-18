from django.db import models

# Create your models here.
# client table
class Customer(models.Model):
    Name = models.CharField(max_length=200, unique=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=200, null=True)
    date_create = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return self.Name

# tag table
class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.name

# product table
class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    )
    prod_Name = models.CharField(max_length=200, null=True)
    prod_price = models.FloatField(max_length=50, null=True)
    prod_category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    prod_desc = models.CharField(max_length=200, null=True)
    date_create = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.prod_Name   


# order table
class Order(models.Model):
    STATUS = (
        ('pending', 'pending'),
        ('out of delivery', 'out of delivery'),
        ('delivery', 'delivery'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=1000, null=True)

    def __str__(self) -> str:
        return self.Product.prod_Name