# Generated by Django 3.2.4 on 2022-11-09 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_user_comment_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='posts',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.post'),
        ),
    ]
