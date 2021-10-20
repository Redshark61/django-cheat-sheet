from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.


def index(response, id):
    ls = ToDoList.objects.get(id=id)
    items = ls.item_set.get(id=1)
    return HttpResponse(f'<h1>{ls.name}</h1><p>{items.text}</p>')
