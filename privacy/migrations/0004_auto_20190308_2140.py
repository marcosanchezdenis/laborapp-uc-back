# Generated by Django 2.1.5 on 2019-03-08 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('privacy', '0003_auto_20190308_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visibility',
            name='abstraccion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='privacy.Abstraction'),
        ),
    ]
