from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils.text import slugify
from django.db.models.signals import post_save
from ckeditor.fields import RichTextField


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = RichTextField()
    habite = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True, unique=True)
    date = models.DateTimeField(blank=True ,default=datetime.datetime.now)
    img = models.ImageField(upload_to='notes-img',blank=True, null=True)



    def save(self, *args, **kwargs):
        if  self.slug is None:
            self.slug = slugify(self.user)
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return '%s'%(self.user)

def creat_profile(sender, **kwargs):
    if kwargs['created'] :
        user_profile = Profile.objects.create(user=kwargs['instance'])


post_save.connect(creat_profile, sender=User)