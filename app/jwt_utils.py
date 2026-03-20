import jwt
import datetime
from django.conf import settings

SECRET_KEY = settings.SECRET_KEY

def generate_token(user):
    expire_time = datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    payload = {
        "user_id" : user.id,
        "username" : user.username,
        "expire" : int(expire_time.timestamp())
    }
    
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    
    return token

def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except:
        return None