# Generated by Django 4.1.2 on 2022-11-18 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0010_alter_payment_unique_together_payment_bname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.CharField(max_length=8),
        ),
    ]