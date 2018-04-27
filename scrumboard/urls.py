from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import re_path, path, include
from django.views.generic import TemplateView
from .api import ListViewSet, CardViewSet

# router = SimpleRouter()
router = DefaultRouter()
router.register(r'lists', ListViewSet)
router.register(r'cards', CardViewSet)

app_name = 'scrumboard'
urlpatterns = [
    re_path('^$', TemplateView.as_view(template_name="scrumboard/index.html"), name="index"),
]
urlpatterns += router.urls
