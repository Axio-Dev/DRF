from django.http import JsonResponse


def api_home(reques, *args, **kwargs):
    return JsonResponse({"message": "Hi There this is your Django API response!!"})