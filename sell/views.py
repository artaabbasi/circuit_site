from django.shortcuts import render
from django.http import JsonResponse
import json
from . import models
def items(request):
    items = models.Item.objects.all()
    l = []
    for item in items:
        d = {
            "id": item.id,
            "name": item.name,
            "description":item.description,
            "price": item.price,
            "image": item.image.path
        }
        l.append(d)
    return JsonResponse(l, content_type='application/json', safe=False)


def item(request, item_id):
    item = models.Item.objects.get(id=item_id)
    d = {
        "id": item.id,
        "name": item.name,
        "description":item.description,
        "price": item.price,
        "image": item.image.path
    }
    return JsonResponse(d, content_type='application/json', safe=False)


def tags(request):
    tags = models.Tag.objects.all()
    l = []
    for item in tags:
        d = {
            "id": item.id,
            "name": item.name,
            "text":item.text,
        }
        l.append(d)
    return JsonResponse(l, content_type='application/json', safe=False)


def tag(request, item_id):
    tag = models.Tag.objects.get(item_id)
    d = {
        "id": tag.id,
        "name": tag.name,
        "text":tag.text,
    }
    return JsonResponse(d, content_type='application/json', safe=False)