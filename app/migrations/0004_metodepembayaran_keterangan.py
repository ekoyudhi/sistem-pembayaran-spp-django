# Generated by Django 2.2.12 on 2021-03-29 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210329_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='metodepembayaran',
            name='keterangan',
            field=models.CharField(max_length=50, null=True),
        ),
    ]