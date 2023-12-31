# Generated by Django 4.2.5 on 2023-09-08 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slack_name', models.CharField(default='Null', max_length=50)),
                ('current_day', models.CharField(default='Friday', max_length=11, verbose_name='Day of the week the api was                                   requested')),
                ('utc_time', models.CharField(default='2023-09-08T16:03:19Z', max_length=100, verbose_name='Datetime request was made')),
                ('track', models.CharField(default='backend', max_length=10)),
                ('github_file_url', models.URLField(default='https://github.com/kelani-culture/HNG-task1/blob/main/my_api/manage.py')),
                ('github_repo_url', models.URLField(default='https://github.com/kelani-culture/HNG-task1')),
                ('status_code', models.IntegerField(default=200)),
            ],
        ),
    ]
