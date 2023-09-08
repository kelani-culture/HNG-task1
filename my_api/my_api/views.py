from .models import UserInfo
from django.http import HttpResponse, JsonResponse
from .utils import current_datetime, get_day


def welcome_view(request):
    return HttpResponse("Welcome to dummy api", status=200)


def user_info(request):
    slack_name = request.GET.get('slack_name')
    track = request.GET.get('track')

    if (slack_name and track):
        dt = UserInfo.objects.update(utc_time=\
                                     current_datetime(),
                                     current_day=get_day()
                                     )
        user_info = UserInfo.objects.all()
        user_data = {
            'slack_name': user_info[0].slack_name,
            'current_day': user_info[0].current_day,
            'utc_time': user_info[0].utc_time,
            'track': user_info[0].track,
            'github_file_url': user_info[0].github_file_url,
            'github_repo_url':user_info[0].github_repo_url,
            'status': user_info[0].status 
        }
        return JsonResponse(user_data, safe=False, status=200)
    else:
        return HttpResponse("Bad request", status=400)