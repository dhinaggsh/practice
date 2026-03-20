from django.http import JsonResponse
import datetime
from .mail import send_mail
from django.views.decorators.csrf import csrf_exempt
import json
import os
from .Machine_Learning.ml import *
from .Machine_Learning.Mlearn import *
from .Machine_Learning.url_ml import *

def get(request):
    return JsonResponse({"Message" : "I am Robot"})

def sync(request):
    data = datetime.datetime.now().time()
    return JsonResponse({"Message" : f"Now data sync time is: {data}"})

@csrf_exempt
def mail_send(request):
    if request.method == 'POST':
        try:
            upload = request.FILES.get('file')
            if not upload:
                return JsonResponse({"error": "file not uploaded"})
            
            os.makedirs("Temporary", exist_ok=True)
            file_path = os.path.join("Temporary", upload.name)
            
            with open(file_path, "wb+") as f:
                for chunk in upload.chunks():
                    f.write(chunk)

            response = send_mail(file_path)
            return JsonResponse({"response": response})
        except Exception as e:
            return JsonResponse({"error": True, "Error Message": str(e)})
    else:
        return JsonResponse({"Message": "Only POST allowed"})
    
from .pagination import page    
  
@csrf_exempt  
def pagination(request):
    try:
        if request.method == 'GET':
            limit=int(request.GET.get("limit", 10))
            page_no=int(request.GET.get("page_no", 0))
            
        elif request.method == 'POST':
            req = json.loads(request.body)
            limit=int(req.get("limit", 10))
            page_no=int(req.get("page_no", 0))
            
        resp = page(limit=limit, page_no=page_no)    
        return JsonResponse({"resp":resp})
    except Exception as e:
        return JsonResponse({"error": True, "Error Message": str(e)})
 
 
from django.shortcuts import render 
def learn(request):
    return render(request, 'learn.html')

@csrf_exempt
def base_ml(request):
    if request.method == 'POST':
        try:
            req = json.loads(request.body)
            resp = base(req)
            return JsonResponse({"resp":resp})
        except Exception as error:
            return JsonResponse({"error":True, "error message":str(error)})
        
@csrf_exempt
def diabetes_ml(request):
    if request.method == 'POST':
        try:
            req = json.loads(request.body)
            resp = diabetes(req)
            return JsonResponse({"resp":resp})
        except Exception as error:
            return JsonResponse({"error":True, "error message":str(error)})
                
@csrf_exempt
def practice_ml(request):
    if request.method == 'GET':
        try:
            resp = practice()
            return JsonResponse({"resp":resp})
        except Exception as error:
            return JsonResponse({"error":True, "error message":str(error)})
            
@csrf_exempt
def sample_ml(request):
    if request.method == 'GET':
        try:
            resp = sample()
            return JsonResponse({"resp":resp})
        except Exception as error:
            return JsonResponse({"error":True, "error message":str(error)})
        
@csrf_exempt
def learn_ml(request):
    if request.method == 'GET':
        try:
            resp = learning_ml()
            return JsonResponse({"resp":resp})
        except Exception as error:
            return JsonResponse({"error":True, "error message":str(error)})
        
@csrf_exempt
def urls_ml(request):
    if request.method == 'GET':
        try:
            resp = url_ml()
            return JsonResponse({"resp":resp})
        except Exception as error:
            return JsonResponse({"error":True, "error message":str(error)})