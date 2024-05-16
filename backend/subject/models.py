from django.db import models
#from django.contrib.auth.models import faculty
#from django.contrib.auth.models import batch

# Create your models here.
class subject(models.Model):
    subid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    #faculty = models.ForeignKey(faculty, default=None)
    #batch = models.ForeignKey(batch, default=None)
