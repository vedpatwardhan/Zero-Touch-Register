from django.db import models
import os
c=os.getcwd()
class visitor(models.Model):

    name = models.CharField(max_length=100)
    entry=models.CharField(max_length=100)
    exit=models.CharField(max_length=100,default="Still in Campus")
    phone = models.CharField(max_length=10)
    email = models.EmailField(default='example@gmail.com')
    address = models.CharField(max_length=100, default='')
    purpose = models.CharField(max_length=100)
    identity = models.CharField(max_length=100)
    Reference=models.CharField(max_length=100,default="")
    aadhar=models.CharField(max_length=16,default="")
    photo=models.ImageField(default=c+"/image.jpg")
    section=models.CharField(max_length=100,default="")
    other=models.CharField(max_length=100,default="NA")
    def __str__(self):  # __str__ for Python 3, __unicode__ for Python 2
        return self.name+"_"+self.entry