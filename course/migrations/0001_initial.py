# Generated by Django 2.1.5 on 2019-01-26 16:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='課程名稱')),
                ('desc', models.CharField(max_length=300, verbose_name='課程簡介')),
                ('image', models.ImageField(upload_to='courses/%Y/%m', verbose_name='封面圖')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加時間')),
            ],
            options={
                'verbose_name': '課程',
                'verbose_name_plural': '課程',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='章節名稱')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加時間')),
                ('desc', models.CharField(max_length=1000, verbose_name='章節內容')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course', verbose_name='課程名稱')),
            ],
            options={
                'verbose_name': '章節',
                'verbose_name_plural': '章節',
            },
        ),
        migrations.CreateModel(
            name='BannerCourse',
            fields=[
            ],
            options={
                'verbose_name': '輪播課程',
                'indexes': [],
                'verbose_name_plural': '輪播課程',
                'proxy': True,
            },
            bases=('course.course',),
        ),
    ]
