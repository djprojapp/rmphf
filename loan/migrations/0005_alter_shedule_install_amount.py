# Generated by Django 4.1.2 on 2022-10-28 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0004_alter_loan_loan_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shedule',
            name='install_amount',
            field=models.DecimalField(decimal_places=2, max_digits=11, null=True),
        ),
    ]
