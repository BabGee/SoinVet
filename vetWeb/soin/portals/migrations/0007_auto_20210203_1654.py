# Generated by Django 3.1.3 on 2021-02-03 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portals', '0006_auto_20210203_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deworming_form',
            name='withdrawal_period',
            field=models.CharField(max_length=100),
        ),
    ]