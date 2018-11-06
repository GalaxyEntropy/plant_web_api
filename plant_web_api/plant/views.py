from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_http_methods
import json
from plant.models import User

@require_http_methods(['GET'])
def show(request):
    # params = json.loads(request.body) #for post
    params = request.GET
    username, password = (params["username"] if "username" in params else None, \
                      params["password"] if "password" in params else None)

    users = User.objects.filter(name=username)
    if not users:
        rs = {
            "err_code": 1,
            "err_desc": "user or password not right"
        }
        return JsonResponse(rs)
    user = users[0]
    rs = {
        "err_code": 0,
        "err_desc": "success",
        "data": [{
            "name":user.name,
            "passwd":user.password
        }]
    }
    return JsonResponse(rs, json_dumps_params={"ensure_ascii": False})
