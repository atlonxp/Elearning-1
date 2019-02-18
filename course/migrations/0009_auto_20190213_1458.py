# Generated by Django 2.1.5 on 2019-02-13 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_words'),
    ]

    operations = [
        migrations.AddField(
            model_name='words',
            name='chinese',
            field=models.CharField(max_length=100, null=True, verbose_name='中文'),
        ),
        migrations.AlterField(
            model_name='words',
            name='description',
            field=models.CharField(max_length=100, null=True, verbose_name='解釋'),
        ),
        migrations.AlterField(
            model_name='words',
            name='example',
            field=models.CharField(max_length=100, null=True, verbose_name='例句'),
        ),
        migrations.AlterField(
            model_name='words',
            name='kk',
            field=models.CharField(max_length=100, null=True, verbose_name='kk音標'),
        ),
        migrations.AlterField(
            model_name='words',
            name='subject',
            field=models.CharField(max_length=100, null=True, verbose_name='詞性'),
        ),
    ]