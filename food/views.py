from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Item
from django.template import loader

# Create your views here.
def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list
    }
    return render(request, 'food/index.html', context)


def item(request):
    return HttpResponse('this is an item view')


def detail(request, pk):
    item = Item.objects.get(id=pk)
    context = {
        'item': item,
    }
    return render(request, 'food/detail.html', context)