# Generated by Django 4.1.2 on 2022-11-07 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0005_alter_bankaccount_acctno_alter_bankaccount_bb_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankaccount',
            name='ppo',
            field=models.CharField(max_length=9, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='ppo',
            field=models.CharField(max_length=9, null=True),
        ),
    ]
