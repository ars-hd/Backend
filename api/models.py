from distutils.command.upload import upload
from random import choices
from django.db import models

# Create your models here.


class BaseModel(models.Model):
    picture = models.ImageField(upload_to='images', null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class Employee(BaseModel):
    name = models.CharField(default='None', null=True, max_length=200)
    designation = models.CharField(default='None', null=True, max_length=200)
    def __str__(self):
        return self.name


class Product(BaseModel):
    title = models.CharField(default='none', null=True, max_length=200)
    typechoice = (
        ('Device', 'device'),
        ('Package', 'package'),
        ('Other', 'other')
    )
    type = models.CharField(default='other', null=True, max_length=200, choices=typechoice)
    price = models.IntegerField(default=0, null=True)
    description = models.CharField(default='none', null=True, max_length=200)
    def __str__(self):
        return self.title