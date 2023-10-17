from django.db import models
from .services import get_path_upload_avatar, validate_size_image
from django.core.validators import FileExtensionValidator
from account.models import CustomUser


class Course(models.Model):
    image = models.ImageField(upload_to="courses/")
    name = models.CharField(max_length=100)
    description = models.TextField()
    continuity = models.CharField(max_length=50)
    number_of_people = models.IntegerField()
    course_program = models.TextField()
    offer = models.ImageField()

    def __str__(self):
        return self.name


class UserContract(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=14)
    passport = models.CharField(max_length=9)
    address = models.CharField(max_length=250)
    offerta_agreement = models.BooleanField(default=False)
    payment_image = models.ImageField(upload_to='mainapp/payment_images')
    transaction_id = models.CharField(max_length=250)
    paid = models.BooleanField(default=False)
    bolib_tolash = models.BooleanField(default=False)
    step = models.IntegerField(max_length=2, default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created', ]
        verbose_name = 'UserContract'
        verbose_name_plural = 'UserContracts'

    def __str__(self):
        return f"{self.user.phone} | {self.course.name}"


class PaymentCost(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    contract = models.ForeignKey(UserContract, on_delete=models.CASCADE)


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=14, unique=True)
    image = models.ImageField(
        upload_to=get_path_upload_avatar, blank=True, null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg']), validate_size_image]
        )
    position = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Newslatter(models.Model):
    class Status(models.TextChoices):
        NEWS = 'NW', 'NEWS'
        BLOG = 'BG', 'BLOG'

    title = models.CharField(max_length=250)
    images = models.ImageField(upload_to='mainapp/newslatter', blank=True, null=True)
    description = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    post_type = models.CharField(max_length=2, choices=Status.choices, default=Status.NEWS)
    choose = models.BooleanField()

    class Meta:
        ordering = ['-title',]
        verbose_name = 'newslatter'
        verbose_name_plural = 'newslatters'

    def __str__(self):
        return self.title


class About(models.Model):
    image = models.ImageField(upload_to='image/about')


class Result(models.Model):
    name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='image/result')
    time_of_studied = models.DateTimeField()
    degree = models.CharField(max_length=50)

    def str(self):
        return self.name