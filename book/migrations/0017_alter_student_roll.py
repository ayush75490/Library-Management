# Generated by Django 3.2.5 on 2021-07-31 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0016_auto_20210801_0309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll',
            field=models.IntegerField(default=587),
        ),
    ]