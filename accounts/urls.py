from django.urls import include, path
from allauth.account.views import confirm_email
from . import views

urlpatterns = [
    #일반 로그인, 회원가입
    path('signup/', views.UserCreate.as_view()), #회원가입
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts-rest/registrations/account-confirm-emil/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
]