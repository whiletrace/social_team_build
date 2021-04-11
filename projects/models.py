from django.conf import settings
from django.db import models
from django.urls import reverse


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

    def get_absolute_url(self):
        return reverse('profiles:detail', kwargs={'pk':self.pk})
