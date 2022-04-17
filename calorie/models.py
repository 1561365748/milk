from django.db import models

# Create your models here.
class User(models.Model):
    user=models.CharField(max_length=20,default='0201120001')
    ingredient=models.CharField(max_length=20,default='芋圆')
    num=models.DecimalField(default=0.0,max_digits = 15,decimal_places = 2)
    class Meta:
       db_table='user'