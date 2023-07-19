# Generated by Django 4.2 on 2023-04-11 10:09

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prod',
            name='img',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['top', 'left'], force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[600, 400], upload_to='main/media/pictures'),
        ),
        migrations.AlterField(
            model_name='prod',
            name='sale_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]