# Generated by Django 4.2.6 on 2024-06-23 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_menutype_materials_menutype_materialsname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menutype',
            name='persons',
            field=models.IntegerField(),
        ),
    ]
