from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class share(models.Model):
    ltype=[('Geo','Geographical Elevation visualization'),
           ('3d','3D scatter plot visualization')]
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField(max_length=240)
    created_at=models.DateTimeField(auto_now_add=True)
    link = models.URLField(max_length=200)
    updated_at=models.DateTimeField(auto_now=True)
    type_of_link=models.CharField(max_length=100,choices=ltype,default='3d')


    def __str__(self):
        return f'{self .user.username} - {self.text[:10]}'