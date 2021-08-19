# Generated by Django 3.2.5 on 2021-07-29 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_alter_student_roll'),
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('b_name', models.CharField(max_length=50)),
                ('publication', models.CharField(max_length=50)),
                ('s_no', models.BigIntegerField()),
                ('edition', models.CharField(max_length=70)),
                ('fees', models.IntegerField()),
                ('status', models.IntegerField(default=1)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='roll',
            field=models.IntegerField(default=544),
        ),
    ]
