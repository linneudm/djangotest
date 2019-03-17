from django.shortcuts import render
import requests
# Create your views here.
from django.core import serializers
import json

#Index consome a API e resgata todos os produtos e operações disponíveis
def index(request):
	url = 'http://localhost:8000/api/products/' 
	url2 = 'http://localhost:8000/api/operations/' 
	r = requests.get(url)
	r2 = requests.get(url2)
	items = r.json()
	items2 = r2.json()
	#Tratamos o JSON pra retornar apenas os campos desejados
	return render(request, 'index.html',
	{"products": [{"id": d["id"], "name":d['name'], "price":d['price'], "quantity":d['quantity']} for d in items], 
	"operations": [{"id": d["id"], "name": d['product'], "quantity":d['quantity']} for d in items2]})
	#return render(request, 'index.html', {"data": items})