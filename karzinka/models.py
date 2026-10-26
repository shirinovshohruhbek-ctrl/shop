from django.db import models
class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
class Client(TimeStampedModel):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=100)
    def __str__(self):
        return self.username
class Product(TimeStampedModel):
    quality_choices = (
        ("basic", "Basic"),
        ("premium", "Premium"),
    )
    quality = models.CharField(default="Basic", max_length=100, choices=quality_choices)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=0)
    quantity = models.PositiveIntegerField(default=1)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name
class Check(TimeStampedModel):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    # client = models.OneToOneField(Client, on_delete=models.CASCADE, related_name='client')
    # product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='product')
    # client = models.ManyToManyField(Client)
    # product = models.ManyToManyField(Product)
    buy_time = models.DateField(auto_now_add=True)
