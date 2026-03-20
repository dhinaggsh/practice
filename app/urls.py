from django.urls import path
from .views import *
from .multiprocess import *
from.payload import *
from .auth_dec import *
from .security import *
from .zoho import *
from .Example import *
from .learn import *


urlpatterns = [
    path('token', view=token_generate, name='token'),
    path('login', view=login_view, name='login'),
    
    path('get', view=jwt_required(get), name='get'),
    path('sync', view=token_required(sync), name='sync'),
    path('process', view=jwt_required(process), name='process'),
    
    path('for', view=jwt_required(for_loop), name='for'),
    path('validate', view=validate_function, name='validate'),
    path('checking', view=checking, name='checking'),
    
    path('multiple', view=multiple_validation, name='multiple'),
    path('df', view=token_required(df_validation), name='df'),
    path('send', view=mail_send, name='send'),
    path('pagination', view=jwt_required(pagination), name='pagination'),
    
    path('zoho', view=zoho, name='zoho'),
    path('register', view=register, name='register'),
    path('get_users', view=get_users, name='get_users'),
    path('loginapi', view=login, name='loginapi'),
    
    
    path('testcase', view=testcase, name='testcase'),
    path('finance_api', view=finance_validation_api, name='finance_api'),
    path('fun', fun),
    path("learn", view=learn, name='learn'),
    
    # Machine Leaening
    path('base_ml', view=base_ml, name='base_ml'),
    path('diabetes_ml', view=diabetes_ml, name='diabetes_ml'),
    path('practice_ml', view=practice_ml, name='practice_ml'),
    path('sample_ml', view=sample_ml, name='sample_ml'),
    path('learn_ml', view=learn_ml, name='learn_ml'),
    path('urls_ml', view=urls_ml, name='urls_ml'),
]

