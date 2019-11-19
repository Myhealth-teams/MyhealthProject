from django.db import models


class Rotations(models.Model):            #轮播
    url = models.CharField(max_length=256)

    class Meta:
        db_table = "rotations"





