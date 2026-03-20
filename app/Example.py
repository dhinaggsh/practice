from datetime import datetime

VALID_CURRENCIES = ["INR", "USD", "EUR"]
VALID_TRANSACTION_TYPES = ["credit", "debit"]


def validate_finance_data(data):

    errors = []

    account_number = data.get("account_number")
    amount = data.get("amount")
    currency = data.get("currency")
    transaction_type = data.get("transaction_type")
    transaction_date = data.get("transaction_date")

    # Account number validation
    if not account_number:
        errors.append("Account number is required")

    elif len(str(account_number)) < 8:
        errors.append("Account number must be at least 8 digits")

    # Amount validation
    if amount is None:
        errors.append("Amount is required")

    elif float(amount) <= 0:
        errors.append("Amount must be greater than zero")

    # Currency validation
    if currency not in VALID_CURRENCIES:
        errors.append("Invalid currency")

    # Transaction type validation
    if transaction_type not in VALID_TRANSACTION_TYPES:
        errors.append("Invalid transaction type")

    # Date validation
    try:
        datetime.strptime(transaction_date, "%Y-%m-%d")
    except:
        errors.append("Invalid date format (YYYY-MM-DD required)")

    if errors:
        return {
            "status": False,
            "errors": errors
        }

    return {
        "status": True,
        "message": "Finance data validated successfully",
        "data" : {
            "account_number" : account_number,
            "amount" : amount,
            "currency" : currency,
            "transaction_type" : transaction_type,
            "transaction_date" : transaction_date
        }
    }

# views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def finance_validation_api(request):

    if request.method != "POST":
        return JsonResponse({
            "status": False,
            "message": "Only POST method allowed"
        })

    try:
        data = json.loads(request.body)

        result = validate_finance_data(data)

        return JsonResponse(result)

    except Exception as e:
        return JsonResponse({
            "status": False,
            "message": str(e)
        })
