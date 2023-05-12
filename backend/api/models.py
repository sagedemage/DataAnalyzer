from django.db import models


# Create your models here.


class User(models.Model):
    email = models.EmailField(null=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=200)


class Table(models.Model):
    name = models.CharField(max_length=200)
    column1_name = models.TextField(max_length=200)
    column2_name = models.TextField(max_length=200)
    user_id = models.IntegerField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Row(models.Model):
    column1_data = models.CharField(max_length=200)
    column2_data = models.TextField(max_length=200)
    table_id = models.IntegerField()

    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
