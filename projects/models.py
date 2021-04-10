from django.conf import settings
from django.db import models


class UserProject(models.Model):
    created_by = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        default="", unique=True,
        on_delete=models.CASCADE
        )
    title = models.CharField(blank=True, default='', max_length=50)
    description = models.TextField()
    timeline = models.CharField(blank=True, default='', max_length=50)
    requirements = models.CharField(blank=True, default='', max_length=50)
