# Generated by Django 4.2.6 on 2024-06-23 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_menutype_materialsname1_menutype_materialsname2'),
    ]

    operations = [
        migrations.AddField(
            model_name='menutype',
            name='img1',
            field=models.ImageField(default=0, upload_to='pics'),
            preserve_default=False,
        ),
    ]
