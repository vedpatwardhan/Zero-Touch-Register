from django.db import models
import os
c=os.getcwd()
class visitor(models.Model):

    name = models.CharField(max_length=100)
    entry=models.CharField(max_length=100)
    dateofentry = models.CharField(max_length=100, default="")
    exit=models.CharField(max_length=100,default="Still in Campus")
    phone = models.CharField(max_length=10)
    email = models.EmailField(default='example@gmail.com')
    address = models.CharField(max_length=100, default='')
    purpose = models.CharField(max_length=100)
    identity = models.CharField(max_length=100)
    other = models.CharField(max_length=100, default="NA")
    Reference=models.CharField(max_length=100,default="")
    aadhar=models.CharField(max_length=16,default="")
    section=models.CharField(max_length=100,default="")
    imagename=models.CharField(max_length=100,default="NA")
    ref_name=models.CharField(max_length=100,default="NA")
    ref_contact=models.CharField(max_length=15,default="NA")
    def __str__(self):  # __str__ for Python 3, __unicode__ for Python 2
        return self.name+"_"+self.entry