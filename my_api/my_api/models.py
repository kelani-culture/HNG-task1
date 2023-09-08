from django.db import models
from .utils import get_day, current_datetime

class UserInfo(models.Model):
    """
    Model for storing user github information
    """
    slack_name = models.CharField(max_length=50,
                                  default="Null")

    current_day = models.CharField(max_length=11,
                                   verboase_name="Day of the week the api was\
                                   requested",
                                   default=get_day())
    
    utc_time = models.CharField(max_length=100,
                                verbose_name="Datetime request was made"
                                default=current_datetime())

    track = models.CharField(max_length=10,
                             default="backend")

    github_file_url = models.URLField(default=\
                                      "https://github.com/kelani-culture/HNG-task1/blob/main/my_api/manage.py")

    github_repo_url = models.URLField(default=\
                                      "https://github.com/kelani-culture/HNG-task1"
                                      )

    status_code = models.IntegerField(default=200)