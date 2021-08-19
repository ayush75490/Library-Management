# Generated by Django 3.2.5 on 2021-07-29 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('roll', models.CharField(max_length=200)),
                ('f_name', models.CharField(max_length=50)),
                ('m_name', models.CharField(max_length=50)),
                ('mobile', models.BigIntegerField()),
                ('email', models.CharField(max_length=70)),
                ('age', models.IntegerField()),
                ('status', models.IntegerField(default=1)),
            ],
        ),
    ]
