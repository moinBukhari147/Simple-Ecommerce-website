from statistics import mode
from django.db import models
from django.forms import CharField

# Create your models here.
class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=70)
    product_desc = models.CharField(max_length=300)
    product_price = models.IntegerField(default=0)
    product_category = models.CharField(max_length=50, default='')
    product_subcatrgory = models.CharField(max_length=50, default='')
    pub_date = models.DateField()
    product_image = models.ImageField(upload_to='shop/pro_images', default='')
    def __str__(self):
        return self.product_name
class contact_us(models.Model):
    contactor_id = models.AutoField(primary_key= True)
    contactor_name = models.CharField(max_length=50)
    contactor_email = models.CharField(max_length=70)
    contactor_phone = models.CharField(max_length=12)
    contactor_query = models.CharField(max_length=1500)
    def __str__(self):
        return self.contactor_name
class newOrders(models.Model):
    orderId = models.BigAutoField
    item_jason = models.CharField(max_length=500, default='')
    chekout_fname = models.CharField(max_length=200, default='')
    chekout_lname = models.CharField(max_length=200, default='')
    chekout_email = models.CharField(max_length=50, default='')
    chekout_phone = models.CharField(max_length=12, default='')
    chekout_address = models.CharField(max_length=300, default='')
    chekout_city = models.CharField(max_length=200, default='')
    chekout_zip = models.CharField(max_length=200, default='')
    chekout_state = models.CharField(max_length=200, default='')
    trackId = models.CharField(max_length=20, default='')
    def __str__(self):
        return self.chekout_fname
class newTrackingUpdate(models.Model):
    track_id = models.AutoField(primary_key=True)
    orderId = models.CharField(max_length=20,default='')
    orderUpdate =  models.CharField(max_length=30, default='none')
    timeUpdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.orderUpdate[:10] + "..."
