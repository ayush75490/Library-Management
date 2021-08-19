# Generated by Django 3.2.5 on 2021-07-31 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0015_alter_student_roll'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bk_is_t',
            old_name='b_is_id',
            new_name='bookname',
        ),
        migrations.RenameField(
            model_name='bk_is_t',
            old_name='b_m_id',
            new_name='std_name',
        ),
        migrations.RemoveField(
            model_name='bk_is_t',
            name='is_upto',
        ),
        migrations.AlterField(
            model_name='bk_is_dt',
            name='fine',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='bk_is_t',
            name='fine',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll',
            field=models.IntegerField(default=669),
        ),
    ]