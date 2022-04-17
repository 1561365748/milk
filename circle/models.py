from django.db import models

# Create your models here.
class Circle(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.CharField(max_length=20,default='某用户')
    saying=models.TextField(default='尚未留言')
    like=models.IntegerField(default=0)
    class Meta:
       db_table='circle'