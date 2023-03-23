from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
STATE_CHOICES = (('Ha Noi', 'Ha Noi'), ('TP Ho Chi Minh', 'TP Ho Chi Minh'), ('Da Nang', 'Da Nang'), ('Hai Phong', 'Hai Phong'), ('Bac Ninh', 'Bac Ninh'), ('Bac Giang',
                 'Bac Giang'), ('Thai Binh', 'Thai Binh'), ('Hue', 'Hue'), ('Nghe An', 'Nghe An'), ('Ba Ria Vung Tau', 'Ba Ria Vung Tau'), ('Thai Nguyen', 'Thai Nguyen'))


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=200)

    def __str__(self):
        return str(self.id)


CATEGORY_CHOICES = (
    ('san pham nam', 'Do cho nam'), ('san pham nu', 'Do cho nu'),
)


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.product.discount * self.quantity


STATUS_CHOICES = (
    ('Duoc chap nhan', 'Duoc chap nhan'),
    ('Dong goi', 'Dong goi'),
    ('Dang van chuyen', 'dang van chuyen'),
    ('da giao hang', 'da giao hang'),
    ('huy bo', 'huy bo')
)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default='chua giai quyet')

    @property
    def total_cost(self):
        return self.product.discount * self.quantity
