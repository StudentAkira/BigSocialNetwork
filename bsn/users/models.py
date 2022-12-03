from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
	pass


class Subscription(models.Model):
	follower = models.ForeignKey(CustomUser, related_name='follower', on_delete=models.CASCADE)
	followed = models.ForeignKey(CustomUser, related_name='followed', on_delete=models.CASCADE)
