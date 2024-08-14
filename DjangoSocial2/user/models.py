from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    point_amt = models.IntegerField(db_column='point_amt', default=0)



