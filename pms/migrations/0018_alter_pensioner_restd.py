# Generated by Django 4.1.2 on 2022-12-05 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0017_pensioner_cpr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pensioner',
            name='restd',
            field=models.DateField(null=True),
        ),
    ]
