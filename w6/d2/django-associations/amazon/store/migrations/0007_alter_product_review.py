# Generated by Django 3.2.4 on 2022-11-09 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20221108_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='review',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.review'),
        ),
    ]
