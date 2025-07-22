from django.db import models

# Create your models here.    
class intern(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.BigIntegerField()
    location=models.CharField(max_length=50)
    college=models.CharField(max_length=100)
    role= (('job','job'),
    ('intern','intern'))
    job=models.CharField(max_length=50, choices=role, default='intern')
    myfile=models.FileField(upload_to="file/", max_length=250, null=True, default=None)
    
    
    
    
