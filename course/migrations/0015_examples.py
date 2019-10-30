# Generated by Django 2.0 on 2019-10-30 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0014_auto_20190424_1132'),
    ]

    operations = [
        migrations.CreateModel(
            name='examples',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examples', models.CharField(blank=True, max_length=100, null=True, verbose_name='例句')),
                ('words', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Words', verbose_name='單字名稱')),
            ],
            options={
                'verbose_name': '例句',
                'verbose_name_plural': '例句',
            },
        ),
    ]