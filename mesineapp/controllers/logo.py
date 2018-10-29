from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from mesineapp.models import *
import json

def logo(request):

    logo = لوگو.objects.filter(حذف = 0).select_related('شناسه_لوگو')
    banner_list=[]
    ban =list(logo.values())
    i=0
    for items in ban:
        banners={}
        banners['id'] = items['شناسه']
        banners['text']=items['متن']
        banners['alt'] = items['جایگزین']
        media = {}
        if (logo[i].شناسه_لوگو.حذف == 0):
            media['image'] = logo[i].شناسه_لوگو.فایل.name
            media['caption']=logo[i].شناسه_لوگو.توضیح
            media['title'] = logo[i].شناسه_لوگو.عنوان
            media['alt'] = logo[i].شناسه_لوگو.جایگزین
            banner_list.append({
            'media' : media,
            'banner_info' : banners
            })
            i=i+1
        else:
            banner_list.append({
            'media' : "Null or deleted",
            'banner_info' : banners
            })
            i=i+1
    result = {
    "ok" : True,
    "status_code": 200,
    "result":banner_list
    }
    return JsonResponse(result,json_dumps_params={'indent': 2},safe=False)



# def logo(request):
