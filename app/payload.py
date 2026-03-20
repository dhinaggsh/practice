from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime


schema = {
    "date" : {"type": "date"},
    "name" : {"type": "varchar", "len":20},
    "notes" : {"type": "varchar", "len": 25},
    "email" : {"type": "varchar", "len": 50},
    "phone_no" : {"type": "number", "len": 10}
}

def validation(data, schema):
    errors = []
    
    for i , rules in schema.items():
        value = data.get(i)
        
        if value is None:
            errors.append(f"field {i} is missing")
            continue
        
        if pd.isna(value):
            errors.append(f"field {i} is missing")
            continue
        
        datatype = rules.get("type")
        
        if datatype == "date":
            try:
                datetime.strptime(value, "%d-%m-%Y")
            except Exception:
                errors.append(f"{i} must be a date format like %Y-%m-%d")
                
        elif datatype == "varchar":
            if not isinstance(value, str):
                errors.append(f"{i} must be a string")
            if "len" in rules and len(value) > rules["len"]:
                errors.append(f"{i} have maximun {rules['len']} digits")
                
        elif datatype == "number":
            value_str = str(value)
            if not value_str.isdigit():
                errors.append(f"{i} must contain only digits")
            elif "len" in rules and len(value_str) != rules["len"]:
                errors.append(f"{i} must be {rules['len']} digits long")
     
    for key in data.keys():
        if key not in schema:
            errors.append(f"Extra field : {key}")
      
    return {
        "is_valid": len(errors) == 0,
        "errors": errors
    }

@csrf_exempt
def validate_function(request):
    if request.method == 'POST':
        try:
            req = json.loads(request.body)
            resp = validation(req, schema)
            
            if resp["is_valid"]:
                return JsonResponse({
                    "result" : resp,
                    "data" : req
                    }, json_dumps_params={"indent": 4})
            else:
                return JsonResponse({
                    "result" : resp,
                    },json_dumps_params={"indent": 4})
        except Exception as e:
            return JsonResponse({"error" : True, "ErrorMessage": str(e)})



@csrf_exempt
def multiple_validation(request):
    if request.method == 'POST':
        try:
            req = json.loads(request.body)
            if isinstance(req, dict):
                req = [req]
            
            results = []
            for index, value in enumerate(req):
                resp = validation(value, schema)
                
                results.append({
                    "row" : index,
                    "results" :resp,
                    "data" : value
                })
            return JsonResponse({
                "data" : results
                }, json_dumps_params={"indent": 4})
                
        except Exception as e:
            return JsonResponse({"error" : True, "ErrorMessage": str(e)})



import pandas as pd

def validate_row(row):
    data = row.to_dict()
    resp = validation(data, schema)
    return {
        "row" : row.name,
        "resp" : resp,
        "data" : data
    }

@csrf_exempt
def df_validation(request):
    if request.method == 'POST':
        try:
            req = json.loads(request.body)
            if isinstance(req, dict):
                req = [req]
            
            pf = pd.DataFrame(req)
            results = pf.apply(validate_row, axis=1).tolist()    
                
            return JsonResponse({
                "data" : results
                }, json_dumps_params={"indent": 4})
                
        except Exception as e:
            return JsonResponse({"error" : True, "ErrorMessage": str(e)})


# [{
#      "date" : "25-02-2026",
#     "name" : "DHINA G",
#     "notes" : "Python Developer",
#     "email" : "abc123@gmail.com",
#     "phone_no" : 1122334455
# },{
#     "date" : "25-02-2025",
#     "name" : "VIJAY TVK",
#     "notes" : "TN CM ",
#     "email" : "tncm2026@gmail.com",
#     "phone_no" : 6677889900
# }]
