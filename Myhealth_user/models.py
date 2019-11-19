from django.db import models

class Users(models.Model):
    u_name = models.CharField(max_length=20,unique=True)
    u_password = models.CharField(max_length=50,unique=True)
    u_tel = models.IntegerField()
    u_image = models.CharField(max_length=256)

    class Meta:
        db_table = "users"