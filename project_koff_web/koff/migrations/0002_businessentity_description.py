# Generated by Django 2.0.3 on 2018-04-23 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('koff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessentity',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description in Markdown'),
        ),
    ]