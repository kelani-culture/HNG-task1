from django.db import models


class UserInfo(models.Model):
    slack_name = models.CharField(max_length=50,
                                  default="Null")
    current_day = models.CharField(max_length=11,
                                   verboase_name="Day of the week the api was\
                                   requested")
    track = models.CharField(max_length=10,
                             default="Backend")
    github_file_url = models.URLField()
    github_repo_url = models.URLField()
    status_code = models.IntegerField(default=200)