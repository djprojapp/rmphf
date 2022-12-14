# Generated by Django 4.1.2 on 2022-12-09 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0020_adjustmenthistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecoveryInstallment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ppo', models.CharField(max_length=9, null=True)),
                ('description', models.CharField(max_length=20, null=True)),
                ('principal', models.IntegerField(null=True)),
                ('installment', models.IntegerField(null=True)),
                ('recovered', models.IntegerField(null=True)),
                ('balance', models.IntegerField(null=True)),
                ('start_date', models.DateField(auto_now_add=True, null=True)),
                ('pensioner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pms.pensioner')),
            ],
        ),
    ]
