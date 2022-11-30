from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Car(models.Model):
    state_number = models.CharField(max_length=15)
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f"{self.make} {self.model} {self.state_number}"


class CarOwner(AbstractUser):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    cars = models.ManyToManyField(Car, through='Ownership', related_name="owners")
    date_of_birth = models.DateTimeField(blank=True, null=True)
    passport_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.second_name} {self.passport_number}"


class DriversLicense(models.Model):
    owner_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    certificate_number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_of_issue = models.DateTimeField()

    def __str__(self):
        return self.certificate_number


class Ownership(models.Model):
    owner_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE, blank=True, null=True)
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Owner: {self.owner_id}, Car: {self.car_id}"
