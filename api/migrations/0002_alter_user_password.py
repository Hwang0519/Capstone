# Generated by Django 4.1.9 on 2023-05-24 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.TextField(),
        ),
    ]