from django.db import models

class Subscription(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    price = models.IntegerField()
    active = models.BooleanField(help_text='Active status', default=True)
    frequency = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
