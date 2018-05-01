from django.urls import path, re_path
from . api import LoginView, LogoutView

# app_name = 'auth_api'
urlpatterns = [
    re_path(r'^login/$', LoginView.as_view()),
    re_path(r'^logout/$', LogoutView.as_view(), name='api_logout'),
]
