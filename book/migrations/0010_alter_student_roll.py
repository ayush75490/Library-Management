# Generated by Django 3.2.5 on 2021-07-29 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0009_alter_student_roll'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll',
            field=models.IntegerField(default=431),
        ),
    ]