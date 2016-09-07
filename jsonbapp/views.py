from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import JSONBModel
# Create your views here.
def index(request):
	return render(request,'jsonbapp/index.html')

def save(request):
	first_name=request.POST['first_name']
	email=request.POST['email']
	JSONBModel.objects.create(jsonbfild={'first_name':first_name,'email':email})
	return HttpResponseRedirect(reverse('jsonbapp:index'))
