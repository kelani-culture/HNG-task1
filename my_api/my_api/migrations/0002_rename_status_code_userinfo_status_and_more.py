# Generated by Django 4.2.5 on 2023-09-08 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='status_code',
            new_name='status',
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='current_day',
            field=models.CharField(default='Friday', max_length=10),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='github_file_url',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='github_repo_url',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='slack_name',
            field=models.CharField(default='Null', max_length=10),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='utc_time',
            field=models.CharField(default='2023-09-08T16:53:24Z', max_length=10),
        ),
    ]
