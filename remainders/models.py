from django.db import models

class Remainder(models.Model):
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
