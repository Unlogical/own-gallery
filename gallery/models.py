from django.db import models

# Create your models here.
from django.utils import timezone


class Image(models.Model):
    src = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()