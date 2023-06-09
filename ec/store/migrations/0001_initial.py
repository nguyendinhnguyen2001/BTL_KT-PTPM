# Generated by Django 4.1.7 on 2023-03-17 16:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("locality", models.CharField(max_length=200)),
                ("address", models.CharField(max_length=200)),
                ("zipcode", models.IntegerField()),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("Ha Noi", "Ha Noi"),
                            ("TP Ho Chi Minh", "TP Ho Chi Minh"),
                            ("Da Nang", "Da Nang"),
                            ("Hai Phong", "Hai Phong"),
                            ("Bac Ninh", "Bac Ninh"),
                            ("Bac Giang", "Bac Giang"),
                            ("Thai Binh", "Thai Binh"),
                            ("Hue", "Hue"),
                            ("Nghe An", "Nghe An"),
                            ("Ba Ria Vung Tau", "Ba Ria Vung Tau"),
                            ("Thai Nguyen", "Thai Nguyen"),
                        ],
                        max_length=200,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("price", models.FloatField()),
                ("discount", models.FloatField()),
                ("description", models.TextField()),
                ("brand", models.CharField(max_length=100)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("san pham nam", "Do cho nam"),
                            ("san pham nu", "Do cho nu"),
                        ],
                        max_length=200,
                    ),
                ),
                ("image", models.ImageField(upload_to="productimg")),
            ],
        ),
        migrations.CreateModel(
            name="OrderPlaced",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.PositiveIntegerField(default=1)),
                ("ordered_date", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Duoc chap nhan", "Duoc chap nhan"),
                            ("Dong goi", "Dong goi"),
                            ("Dang van chuyen", "dang van chuyen"),
                            ("da giao hang", "da giao hang"),
                            ("huy bo", "huy bo"),
                        ],
                        default="chua giai quyet",
                        max_length=50,
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.customer"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.product"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.PositiveIntegerField(default=1)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.product"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
