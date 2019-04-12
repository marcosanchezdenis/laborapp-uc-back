# Generated by Django 2.1.7 on 2019-03-14 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('privacy', '0004_auto_20190308_2140'),
        ('provider', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='providerdata',
            name='visibility',
        ),
        migrations.AddField(
            model_name='providerdata',
            name='visibility',
            field=models.ManyToManyField(to='privacy.Visibility'),
        ),
    ]
