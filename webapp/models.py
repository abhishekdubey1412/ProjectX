from django.db import models

# Create your models here.
class Records(models.Model):
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True) 
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=20, blank=False)
    state = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=20, blank=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name