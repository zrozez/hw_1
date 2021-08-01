from django.db import models

from hospital.models import Hospital

class Ask(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL,
                            null=True, related_name='asks')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)


    def __str__(self):
        return f'Ask by {self.name} on {self.hospital}'
    
