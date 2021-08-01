from django.db import models
from django.shortcuts import reverse


class Hospital(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()

    def get_absolute_url(self):
        return reverse('hospital_detail_url', kwargs={'id': self.id})

