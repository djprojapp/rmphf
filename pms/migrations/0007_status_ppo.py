# Generated by Django 4.1.2 on 2022-11-07 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0006_bankaccount_ppo_payment_ppo'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='ppo',
            field=models.CharField(max_length=9, null=True),
        ),
    ]
