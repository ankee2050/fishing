from django.urls import path
from .views import *

urlpatterns = [
	path('',get_private, name='get_private'),
	path('get_plan',get_plan, name='get_plan'),
	path('get_detail',get_detail, name='get_detail')
]