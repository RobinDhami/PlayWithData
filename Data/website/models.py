from django.db import models

# Create your models here.

class Member(models.Model):
    first_name= models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    passwd=models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name+" " + self.last_name