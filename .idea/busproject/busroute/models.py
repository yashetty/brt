from django.db import models


from django.db import models
from django.db.models import CharField


class route(models.Model):
    idroute =models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    distfromsrc= models.CharField(max_length=20)
    arrival = models.CharField(max_length=20)
    class Meta:
        db_table = "route"

class register(models.Model):
    name =models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    mobileno=models.CharField(max_length=20)
    password= models.CharField(max_length=20)
    class Meta:
        db_table = "register"