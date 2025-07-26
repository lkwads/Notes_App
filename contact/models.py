from django.db import models
from phone_field import PhoneField


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField(null=False, blank=False)
    message = models.TextField()
    add_at = models.DateField(auto_now_add=True)



    def __str__(self):
        return self.name