# Generated by Django 3.2.4 on 2022-11-09 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20221108_2027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='post',
        ),
    ]
