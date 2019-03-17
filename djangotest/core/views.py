from django.shortcuts import render
import requests
# Create your views here.
from django.core import serializers
import json

def index(request):
	url = 'http://localhost:8000/products/' 
	r = requests.get(url)
	items = r.json()
	#print(books_list)
	#return books_list
	#return render(request, 'index.html', {"data": [d['name'] for d in items]})
	return render(request, 'index.html', {"data": items})