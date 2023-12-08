from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    phone_number = models.CharField(max_length=13, unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number',
        )
    ])

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'



class Room(models.Model):
    name = models.CharField(max_length=55, unique=True)
    student_number = models.IntegerField(default=10)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    full_name = models.CharField(max_length=55, blank=False)
    student = models.ForeignKey(to='Student', on_delete=models.PROTECT)
    room = models.ForeignKey(to='room', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(to='User',on_delete=models.CASCADE)
    bio = models.TextField()
    subjects = models.CharField(max_length=55)
    salary = models.PositiveIntegerField(default=100000)
    start_work_time = models.TimeField()
    end_work_time = models.TimeField()
    age = models.IntegerField(default=18)
    photo_img = models.ImageField(upload_to='photos-teacher/', null=True, blank=True)
    WORK_DAY_CHOICES = (
        ('Dushanba','Dushanba'),
        ('Seshanba','Seshanba'),
        ('Payshanba','Payshanba'),
        ('Juma','Juma'),
        ('Shanba','Shanba'),
        ('Yakshanba','Yakshanba'),
    )
    work_day = models.CharField(max_length=55, choices=WORK_DAY_CHOICES)

    def __str__(self):
        return self.full_name


class Student(models.Model):
    fullname  = models.CharField(max_length=55, blank=False)
    age = models.IntegerField(7)
    phone_number = models.CharField(max_length=13, unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    parent_number = models.CharField(max_length=13, unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    extra_info = models.TextField()


class Employee(models.Model):
    full_name = models.CharField(max_length=25, blank=False)
    salary = models.PositiveIntegerField(default = 100000)
    start_work_time = models.TimeField()
    end_work_time = models.TimeField()
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
    status = models.IntegerField(default=5,choices=(
        (1,'Direktor'),
        (2,'Manager'),
        (3,'Admin'),
        (4,'Teacher'),
        (5,'Other'),
    ))
    bio = models.TextField()

    def __str__(self):
        return self.full_name


class Info(models.Model):
    name = models.CharField(max_length=55, blank=False)
    adress = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13, unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    email = models.CharField(max_length=75)


