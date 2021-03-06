from django.db import models
class Profile(models.Model):
    name=models.CharField(max_length=50)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    skills=models.CharField(max_length=50)