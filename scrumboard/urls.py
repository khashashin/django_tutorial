from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import re_path, path, include
from django.views.generic import TemplateView
from .api import ListViewSet, CardViewSet
from django.views.decorators.csrf import ensure_csrf_cookie

# router = SimpleRouter()
router = DefaultRouter()
router.register(r'lists', ListViewSet)
router.register(r'cards', CardViewSet)

app_name = 'scrumboard'
urlpatterns = [
    path('', ensure_csrf_cookie(TemplateView.as_view(template_name="scrumboard/index.html")), name="index"),
]
urlpatterns += router.urls
