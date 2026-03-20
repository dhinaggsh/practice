from django.conf import settings
from functools import wraps
import json
import jwt
import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def token_generate(request):
    data = json.loads(request.body)
    secret = data.get("secret_key")
    
    if secret != settings.SECRET_KEY:
        return JsonResponse({"error" : "UnAuthorized, Invalid Token"}, status=401)
    
    payload = {
        "type" : "security",
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")

    return JsonResponse({"token": token})


def token_required(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return JsonResponse({"error": "Token required"}, status=401)

        try:
            token = auth_header.split(" ")[1]
        except:
            return JsonResponse({"error": "Invalid token format"}, status=401)

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            if payload.get("type") != "security":
                return JsonResponse({"error": "Invalid token type"}, status=403)
            
        except jwt.ExpiredSignatureError:
            return JsonResponse({"error": "Token expired"}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({"error": "Invalid token"}, status=401)

        return func(request, *args, **kwargs)
    return wrapper


@csrf_exempt
def testcase(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        if username == "admin" and password == "1234":
            return JsonResponse({"message" : "Login Success"})
        else:
            return JsonResponse({"error" : "Invalid Credentials"})

