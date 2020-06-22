from .views import *
from django.urls import path

app_name = 'xtb'

urlpatterns = [
    path('', index, name='index'),
    path('page/<str:page_name>', page_views, name='page_views'),
    path('test/', ajax_test, name='ajax_test'),
]

