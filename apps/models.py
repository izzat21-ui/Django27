from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models import Model, ImageField, CharField, IntegerChoices, IntegerField, DecimalField, TextField, \
    FileField, ForeignKey, CASCADE, TextChoices
from django.db.models.fields import EmailField, BooleanField, DateTimeField
from apps.error_messages import name_card, price_car, speed_car, km_car, number_user


class Course(Model):
    main_image = ImageField(upload_to='images/courses/')
    title = CharField(max_length=255)
    author = CharField(max_length=255)
    review_count = IntegerField(default=0)
    price = DecimalField(max_digits=10, decimal_places=2)
    description = TextField()
    video = FileField(upload_to='videos/courses/', default='1')

    # category = ForeignKey('apps.Category', on_delete=CASCADE, related_name='courses')

    def __str__(self):
        return self.title


@property
def avg_rating(self):
    ratings = list(map(lambda x: x[0], self.course_ratings.values_list('rating')))
    avg = 0
    if ratings:
        avg = sum(ratings) / len(ratings)
    return round(avg, 1)


# class Category(Model):
#
#     class Meta:
#         verbose_name_plural = "Categories"
#
#     image = ImageField(upload_to='images/categories/')
#     name = CharField(max_length=255)
#
#     def __str__(self):
#         return self.name


class CourseRating(Model):
    class RatingType(IntegerChoices):
        ONE = 1, "1"
        TWO = 2, "2"
        THREE = 3, "3"
        FOUR = 4, "4"
        FIVE = 5, "5"

    course = ForeignKey('apps.Course', on_delete=CASCADE, related_name='course_ratings')
    rating = IntegerField(choices=RatingType.choices)
    user = ForeignKey('apps.User', on_delete=CASCADE, related_name='course_ratings')

    def __str__(self):
        return self.rating


class Film(Model):
    title = CharField(max_length=255)
    video = FileField(upload_to='videos/films/', default='1')
    main_image = ImageField(upload_to='images/films/')
    duration = CharField(max_length=255)

    def __str__(self):
        return self.title


class todo_lists(Model):
    title = CharField(max_length=255)


class Region(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class District(Model):
    name = CharField(max_length=255)
    region = ForeignKey('apps.Region', CASCADE, related_name='districts')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)


class Cars(Model):
    class Meta:
        verbose_name_plural = "Cars"

    name = CharField(max_length=55, error_messages=name_card)
    price = DecimalField(max_digits=10, decimal_places=2, error_messages=price_car)
    speed = DecimalField(max_digits=10, decimal_places=2, error_messages=speed_car)  #
    km = DecimalField(max_digits=10, decimal_places=2, error_messages=km_car)


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


class Category(Model):
    class Type(TextChoices):
        INCOME = 'income', 'Income'
        EXPENSE = 'expense', 'Expense'

    name = CharField(max_length=255)
    icon = CharField(max_length=255)
    type = CharField(max_length=255, choices=Type)


class Wallet(Model):
    amount = DecimalField(max_digits=10, decimal_places=2)
    category = ForeignKey('apps.Category', CASCADE, related_name='wallets')
    description = TextField()
    type = CharField(max_length=55, choices=Category.Type)
    wallet_ad = DateTimeField(auto_now_add=True)
    user = ForeignKey('apps.User', CASCADE, related_name='wallets')


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
