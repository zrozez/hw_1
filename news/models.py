from django.db import models
from hospital.models import Hospital
from django.shortcuts import reverse

class News(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    hospital = models.ManyToManyField(Hospital, related_name='hospital')


    def get_absolute_url(self):
        return reverse('news_detail_url', kwargs={'id': self.id})
