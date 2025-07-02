from django.db import models

# Create your models here.
class Files(models.Model):
    SUBJECT_CHOICES = [
        ('Applied Mechanics', 'Applied Mechanics'),
        ('C Programming', 'C Programming'),
        ('Mathematics', 'Mathematics'),
        ('Drawing I', 'Drawing I'),
        ('Physics', 'Physics'),
        ('Basic Electrical', 'Basic Electrical'),
    ]

    subject = models.CharField(max_length=100, choices=SUBJECT_CHOICES, unique=True  )
    adminupload = models.FileField(upload_to="media")

    def __str__(self):
        return self.subject
