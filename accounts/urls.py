from django.urls import include, path
from . import views

urlpatterns = [
    #일반 로그인, 회원가입
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls'))
]