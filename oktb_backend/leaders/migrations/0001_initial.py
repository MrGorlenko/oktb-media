# Generated by Django 3.1.2 on 2020-10-13 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('img', models.ImageField(upload_to='static/leaders')),
                ('audience', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
