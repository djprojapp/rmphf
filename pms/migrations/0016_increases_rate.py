# Generated by Django 4.1.2 on 2022-11-29 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0015_remove_pensioner_fpname_pensioner_lpd'),
    ]

    operations = [
        migrations.AddField(
            model_name='increases',
            name='rate',
            field=models.CharField(max_length=4, null=True),
        ),
    ]