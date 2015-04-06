from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Entry(models.Model):
    timestamp = models.DateTimeField(default=now)
    contents = models.CharField(max_length=1000)
    owner = models.ForeignKey(User)
