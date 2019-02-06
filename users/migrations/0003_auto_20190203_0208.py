# Generated by Django 2.1.5 on 2019-02-02 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190203_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='department',
            field=models.CharField(choices=[('應用英語', '應用英語'), ('應用日語', '應用日語'), ('應用中文', '應用中文'), ('資訊工程', '資訊工程'), ('資訊管理', '資訊管理'), ('護理', '護理')], default=1, max_length=10, verbose_name='科系'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='grade',
            field=models.CharField(choices=[('一年級', '一年級'), ('二年級', '二年級'), ('三年級', '三年級'), ('四年級', '四年級'), ('五年級', '五年級')], default=1, max_length=10, verbose_name='年級'),
        ),
    ]
