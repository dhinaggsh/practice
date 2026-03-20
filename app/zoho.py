from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def zoho(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        name = data.get("name")
        age = data.get("age")
        email = data.get("email")
        
        if not name or not age:
            return JsonResponse({"error" : "name or age is missing"})
        if "@" not in email:
            return JsonResponse({"error" : "email invalid"})

        status = "adult" if age > 18 else "minor"
        
        return JsonResponse({
            "name" : name,
            "age" : age,
            "status" : status
        })
        
    else:
        return JsonResponse({"error" : "Only POST method allowed"})

users =[]

@csrf_exempt
def register(request):
    data = json.loads(request.body)
    
    name = data.get("name")
    age = int(data.get("age"))
    email = data.get("email")
    password = data.get("password")
    
    if not name or age is None or not email or not password:
        return JsonResponse({"error" : "field is missing"})
    if "@" not in email or ".com" not in email:
        return JsonResponse({"error" : "email invalid"})
    if len(password) < 6:
        return JsonResponse({"error" : "password must be minimum 6 characters"})
    if age < 18:
        return JsonResponse({"error": "User must be 18+ to register"})
    
    for i in users:
        if email == i['email']:
            return JsonResponse({"error" : "email already exists"})
    
    users.append({"name":name, "age":age, "email":email, "password":password})
    print(users)
    return JsonResponse({
        "message": "User registered successfully",
        "total_users" : len(users)
    })  


@csrf_exempt
def get_users(request):
    data = []
    print(users)
    for i in users:
        data.append({
                "name" : i["name"],
                "email" : i["email"]
        })
    return JsonResponse({"users" : data})

@csrf_exempt
def login(request):
    data = json.loads(request.body)

    email = data.get("email")
    password = data.get("password")
    for i in users:
        if email == i["email"] and password == i["password"]:
            return JsonResponse({
                "message": "Login Successful"
            })

    return JsonResponse({
        "error": "invalid email or password"
    }, status=401)