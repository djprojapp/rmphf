# Generated by Django 4.1.2 on 2022-11-08 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0008_remove_payment_period_from_remove_payment_period_to_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='payment',
            unique_together={('month', 'year')},
        ),
    ]