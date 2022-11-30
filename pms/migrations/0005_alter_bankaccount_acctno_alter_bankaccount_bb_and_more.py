# Generated by Django 4.1.2 on 2022-11-07 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0004_bankaccount_remove_bankfamily_pensioner_delete_bank_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='acctno',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='bb',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='bname',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='payment_ratio',
            field=models.FloatField(max_length=4, null=True),
        ),
    ]
