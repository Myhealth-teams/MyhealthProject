

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysRole',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=50)),
                ('role_code', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'sys_role',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysUser',
            fields=[
                ('sy_id', models.AutoField(primary_key=True, serialize=False)),
                ('sy_name', models.CharField(blank=True, max_length=50, null=True)),
                ('auth_string', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'sys_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysUserRole',
            fields=[
                ('sr_id', models.AutoField(primary_key=True, serialize=False)),
                ('role_id', models.IntegerField(blank=True, null=True)),
                ('sy_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sys_user_role',
                'managed': False,
            },
        ),
    ]
