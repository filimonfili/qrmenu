# Generated by Django 4.2.6 on 2024-06-23 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_menutype_descd'),
    ]

    operations = [
        migrations.AddField(
            model_name='menutype',
            name='materials',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menutype',
            name='materialsname',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menutype',
            name='persons',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
