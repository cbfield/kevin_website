# Generated by Django 2.1.5 on 2019-01-31 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home_image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='vimeo_link',
            name='video',
            field=models.TextField(),
        ),
    ]
