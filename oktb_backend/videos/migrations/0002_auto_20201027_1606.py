# Generated by Django 3.1.2 on 2020-10-27 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]