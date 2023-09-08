from django.utils import timezone
from datetime import datetime


def get_day():
    today = datetime.today()
    return today.strftime("%A")


def current_datetime():
    return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")