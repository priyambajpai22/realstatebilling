# Generated by Django 4.0.2 on 2022-03-04 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_mapimage_user_is_mapper_mapmodel_mapimage_map_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='mapimage',
            name='name',
            field=models.CharField(default='this is not', max_length=200),
            preserve_default=False,
        ),
    ]
