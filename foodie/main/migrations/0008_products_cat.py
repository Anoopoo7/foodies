# Generated by Django 3.1.6 on 2021-07-18 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210718_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='cat',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]