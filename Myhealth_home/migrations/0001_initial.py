# Generated by Django 2.0.6 on 2019-11-19 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rotations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'rotations',
            },
        ),
    ]
