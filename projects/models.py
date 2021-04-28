from django.conf import settings
from django.db import models
from django.urls import reverse


class UserProject(models.Model):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        default="",
        on_delete=models.CASCADE
        )
    title = models.CharField(blank=True, default='', max_length=50)
    description = models.TextField()
    timeline = models.CharField(blank=True, default='', max_length=50)
    requirements = models.CharField(blank=True, default='', max_length=50)

    def get_absolute_url(self):
        return reverse('profiles:detail', kwargs={'pk':self.pk})


class Position(models.Model):
    project = models.ForeignKey(UserProject, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()


class Applicant(models.Model):
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.CASCADE)
    Status = models.BooleanField(default='')
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
