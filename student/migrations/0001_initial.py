# Generated by Django 2.1.13 on 2019-11-11 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studName', models.CharField(max_length=100, verbose_name='stud_name')),
                ('studAge', models.IntegerField(verbose_name='stud_age')),
                ('studAddress', models.CharField(max_length=100, verbose_name='stud_address')),
                ('studCollege', models.CharField(max_length=100, verbose_name='stud_college')),
                ('studEmail', models.EmailField(max_length=100, unique=True, verbose_name='stud_email')),
                ('studDept', models.CharField(max_length=100, verbose_name='stud_dept')),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]