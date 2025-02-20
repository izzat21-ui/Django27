from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models import Model, ImageField, CharField, IntegerChoices, IntegerField, DecimalField, TextField, \
    FileField, ForeignKey, CASCADE, TextChoices
from django.db.models.fields import EmailField, BooleanField, DateTimeField
from apps.error_messages import name_card, price_car, speed_car, km_car, number_user



class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    phone = CharField(max_length=20, error_messages=number_user)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    email = EmailField("email address", unique=True)
    is_active = BooleanField(default=False)





class Transaction(Model):
    class Type(TextChoices):
        COMPLETED = 'completed', 'Completed'
        PENDING = 'pending', 'Pending'

    date = DateTimeField(auto_now_add=True)
    name = CharField(max_length=255)
    amount = DecimalField(max_digits=10, decimal_places=2)
    status = CharField(max_length=255, choices=Type)

class Cart(Model):
    photo = CharField(max_length=255)
    product = CharField(max_length=255)
    Qty = IntegerField()
    price = DecimalField(max_digits=10, decimal_places=2)
    total = DecimalField(max_digits=10, decimal_places=2)
