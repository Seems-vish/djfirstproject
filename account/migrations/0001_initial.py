# Generated by Django 2.2.6 on 2019-10-10 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accHolderName', models.CharField(max_length=100, verbose_name='acc_holder_name')),
                ('accBalance', models.FloatField(verbose_name='acc_bal')),
                ('accType', models.CharField(max_length=10, verbose_name='acc_type')),
            ],
        ),
    ]
