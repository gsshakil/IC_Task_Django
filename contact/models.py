from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField(blank=True)
    city = models.CharField(null=True, max_length=100)
    country = models.CharField(null=True, max_length=100)
    
    def __str__(self):
        return (self.name)