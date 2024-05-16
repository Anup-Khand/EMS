from django.db import models
#from django.contrib.auth.models import batch
#from django.contrib.auth.models import faculty
# Create your models here.
class Students(models.Model):
    stuid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
   # batch = models.ForeignKey(batch, default = None)
    #faculty = models.ForeignKey(faculty, default = None)
    gender = models.CharField(max_length=255)
    profile_pic = models.FileField()
