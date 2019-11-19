from django.db import models

class Users(models.Model):
    u_name = models.CharField(max_length=20,null=True)
    u_password = models.CharField(max_length=50)
    u_tel = models.CharField(max_length=11,unique=True,null=False)
    u_image = models.CharField(max_length=256,default=None,null=True)

    class Meta:
        db_table = "users"