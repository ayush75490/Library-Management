# Generated by Django 3.2.5 on 2021-07-29 22:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0010_alter_student_roll'),
    ]

    operations = [
        migrations.CreateModel(
            name='bk_is_dt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('b_is_id', models.BigIntegerField()),
                ('b_m_id', models.BigIntegerField()),
                ('is_upto', models.BigIntegerField()),
                ('re_date', models.DateField(default=datetime.date(2021, 7, 30))),
                ('fine', models.BigIntegerField()),
                ('status', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='bk_is_t',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('b_is_id', models.BigIntegerField()),
                ('b_m_id', models.BigIntegerField()),
                ('is_upto', models.BigIntegerField()),
                ('re_date', models.DateField(default=datetime.date(2021, 7, 30))),
                ('fine', models.BigIntegerField()),
                ('status', models.IntegerField(default=1)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='roll',
            field=models.IntegerField(default=801),
        ),
    ]
