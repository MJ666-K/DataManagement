# Generated by Django 4.1.7 on 2023-04-09 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DepartUserPretty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
            ],
        ),
        migrations.AlterField(
            model_name='prettynum',
            name='level',
            field=models.SmallIntegerField(choices=[(3, '3级'), (4, '4级'), (2, '2级'), (1, '1级')], default=1, verbose_name='级别'),
        ),
        migrations.AlterField(
            model_name='prettynum',
            name='status',
            field=models.SmallIntegerField(choices=[(2, '未使用'), (1, '已占用')], default=2, verbose_name='状态'),
        ),
    ]
