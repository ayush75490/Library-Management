# Generated by Django 3.2.5 on 2021-07-31 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0014_auto_20210801_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll',
            field=models.IntegerField(default=1224),
        ),
    ]
