# Generated by Django 3.2.5 on 2021-08-01 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0018_auto_20210801_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll',
            field=models.IntegerField(default=661),
        ),
    ]