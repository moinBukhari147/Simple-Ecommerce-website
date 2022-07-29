from pyexpat import model
from statistics import mode
from django.db import models
from django.forms import CharField

# Create your models here.
class blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    author_name = models.CharField(max_length=30,default='No Name')
    post_title =  models.CharField(max_length=80, default='No Title')
    post_heading1 =  models.CharField(max_length=100, default='No Heading')
    post_heading2 =  models.CharField(max_length=100, default='No heading')
    post_heading3 =  models.CharField(max_length=100, default='No Heading')
    post_content1 =  models.CharField(max_length=300, default='No content')
    post_content2 =  models.CharField(max_length=300, default='No content')
    post_content3 =  models.CharField(max_length=300, default='No content')
    post_dateTime = models.DateTimeField(auto_now_add=True)
    post_thumbnail = models.ImageField(upload_to='shop/pro_images', default='')
    def __str__(self):
        return self.post_title
