# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class SysRole(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=50)
    role_code = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'sys_role'


class SysUser(models.Model):
    sy_id = models.AutoField(primary_key=True)
    sy_name = models.CharField(max_length=50, blank=True, null=True)
    auth_string = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user'


class SysUserRole(models.Model):
    sr_id = models.AutoField(primary_key=True)
    role = models.ForeignKey(SysRole, models.DO_NOTHING, blank=True, null=True)
    sy = models.ForeignKey(SysUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user_role'
