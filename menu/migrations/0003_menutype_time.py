# Generated by Django 4.2.6 on 2024-06-23 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_menutype_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='menutype',
            name='time',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]