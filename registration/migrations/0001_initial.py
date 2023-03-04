# Generated by Django 2.2.9 on 2022-12-21 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('email', models.CharField(max_length=30, unique=True)),
                ('role', models.CharField(default='Guest', max_length=30)),
                ('phone_num', models.BigIntegerField(unique=True)),
                ('joiningDate', models.DateField()),
            ],
            options={
                'db_table': 'EMPLOYEE_MASTER',
                'ordering': ['role'],
            },
        ),
    ]
