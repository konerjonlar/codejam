# Generated by Django 3.2.8 on 2021-10-24 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='site',
            field=models.URLField(blank=True, verbose_name='Proje Url'),
        ),
    ]
