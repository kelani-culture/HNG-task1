from django.db import models
from .utils import get_day, current_datetime


class UserInfo(models.Model):
    slack_name = models.CharField(max_length=10,
                                  default="Null")
    current_day = models.CharField(max_length=10,
                                   default=get_day())
    utc_time = models.CharField(max_length=10,
                                    default=current_datetime())
    track = models.CharField(max_length=10,
                             default="backend")
    github_file_url = models.URLField()
    github_repo_url = models.URLField()
    status = models.IntegerField(default=200)