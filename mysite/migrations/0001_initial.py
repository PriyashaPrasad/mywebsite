# Generated by Django 3.0.8 on 2020-07-27 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('summary', models.CharField(max_length=400)),
                ('title', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=500)),
            ],
        ),
    ]
