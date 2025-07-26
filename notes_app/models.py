from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils.text import slugify
from ckeditor.fields import RichTextField
# Create your models here.
class Notes(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=35)
    slug = models.SlugField(null=True, blank=True)
    content = RichTextField()
    created = models.DateTimeField(blank=True, default=datetime.datetime.now)
    active = models.BooleanField(default=True)
    tags = models.CharField(blank=True, max_length=45)
    img = models.ImageField(upload_to='notes-img/', blank=True)
    
    def save(self, *args, **kwargs):
        if  self.slug is None:
            self.slug = slugify(self.title)
        super(Notes, self).save(*args, **kwargs)

    def __str__(self):
        return self.title



