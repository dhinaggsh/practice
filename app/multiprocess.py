from multiprocessing import Pool
import os, json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from concurrent.futures import ThreadPoolExecutor
import time

values = [
    {
        "data": [{"id":1,"title":"Essence Mascara Lash Princess","category":"beauty","price":9.99}],
        "company_id": 101
    },
    {
        "data": [{"id":2,"title":"Eyeshadow Palette with Mirror","category":"beauty","price":19.99}],
        "company_id": 102 
    }
]

def process_company(company):
    company_id = company["company_id"]
    data = company.get("data", [])
    
    titles = [item["title"] for item in data]
    return {"company_id": company_id, "titles": titles}

@csrf_exempt  
def process(request):
    try:
        start_time = time.time()
        with ThreadPoolExecutor(max_workers=5) as executor:
            results = list(executor.map(process_company, values))
            print(results)
            time.sleep(2)
        end_time = time.time()
        
        total_time = end_time - start_time
        print(f"Total time taken {total_time:.4f} seconds")
        
        return JsonResponse({"res": results, "total":f"{total_time:.4f} seconds"})
    except Exception as e:
        return JsonResponse({"Error": True, "Errormessage": str(e)})

@csrf_exempt
def for_loop(request):
    try:
        start_time = time.time()
        data = []
        for i in values:
            result = process_company(i)
            data.append(result)
            time.sleep(2)
        end_time = time.time()
        total_times = end_time - start_time
        
        print("result", data)
        print(f"Total time taken {total_times:.4f} seconds")
        
        return JsonResponse({"res":data, "total_time":f"{total_times:.4f} seconds"})
    
    except Exception as error:
        return JsonResponse({"error":True, "ErrorMessage":str(error)})
    

from .payload import validation

data = {
    "date" : {"type": "date"},
    "name" : {"type": "varchar", "len":20},
    "phone_no" : {"type": "number", "len": 10}
}

@csrf_exempt
def checking(request):
    if request.method == 'POST':
        try:
            req = json.loads(request.body)
            resp = validation(req, data)
            return JsonResponse({
                "data" : req,
                "checking" : resp
            })
        except Exception as error:
            return JsonResponse({"error":True, "ErrorMessage":str(error)})