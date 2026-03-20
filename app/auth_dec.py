from django.http import JsonResponse
from functools import wraps
from django.views.decorators.csrf import csrf_exempt
import jwt, json, datetime
from django.conf import settings
from django.contrib.auth import authenticate


@csrf_exempt
def login_view(request):

    if request.method == "POST":

        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")

        user = authenticate(username=username, password=password)
        if user is None:
            return JsonResponse({"error": "Invalid credentials"}, status=401)

        token = generate_token(user)
        return JsonResponse({
            "token": token
        })
           
SECRET_KEY = settings.SECRET_KEY

def generate_token(user):
    payload = {
        "type" : "user",   # for check token
        "user_id" : user.id,
        "username" : user.username,
        "exp" : datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }
    
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    
    return token

def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except:
        return None

def jwt_required(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return JsonResponse({"error": "Token required"}, status=401)

        try:
            token = auth_header.split(" ")[1]
        except:
            return JsonResponse({"error": "Invalid token format"}, status=401)
        
        payload = verify_token(token)

        if payload is None:
            return JsonResponse({"error": "Invalid or expired token"}, status=401)
        if payload.get("type") != "user":
            return JsonResponse({"error": "Invalid token type"}, status=403)
        request.user_payload = payload

        return func(request, *args, **kwargs)
    return wrapper