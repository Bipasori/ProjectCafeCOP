from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

active_roles = (
    ("user", "user"),
    ("manager", "manager"),
    ("partner", "partner")
)

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    membername = models.CharField(db_column='membername', max_length=50, default='')
    role = models.CharField(max_length=20, choices=active_roles, default="user")
    phone_no = models.CharField(db_column='phone_no', null=True, max_length=100, default='')
    zipcode = models.CharField(db_column='zipcode', null=True, max_length=10, default='')
    address = models.CharField(db_column='address', null=True, max_length=1024, default='')
    address_detail = models.CharField(db_column='address_detail', null=True, max_length=255, default='')
    usage_flag = models.CharField(max_length=10, default='1')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
