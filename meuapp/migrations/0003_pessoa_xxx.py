# Generated by Django 3.0.4 on 2020-03-10 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meuapp', '0002_auto_20200310_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='xxx',
            field=models.CharField(max_length=20, null=True),
        ),
    ]