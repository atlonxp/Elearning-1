# Generated by Django 2.1.5 on 2019-02-04 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_is_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='desc',
            field=models.TextField(verbose_name='章節內容'),
        ),
    ]