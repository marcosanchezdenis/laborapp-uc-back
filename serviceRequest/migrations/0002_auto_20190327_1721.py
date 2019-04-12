# Generated by Django 2.1.7 on 2019-03-27 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('serviceRequest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='provider.Provider'),
        ),
    ]