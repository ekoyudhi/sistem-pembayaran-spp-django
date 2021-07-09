# Generated by Django 2.2.12 on 2021-03-28 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20210328_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='siswa',
            name='nama',
            field=models.CharField(max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]