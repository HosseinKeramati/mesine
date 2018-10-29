from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from mesineapp.models import *
import json


def banner(request):

    banner = بنر.objects.filter(نوع_id = 5 , حذف = 0).select_related('شناسه_بنر')
    banner_list=[]
    ban =list(banner.values())
    i=0
    for items in ban:
        banners={}
        banners['id'] = items['شناسه']
        banners['title']=items['عنوان']
        banners['subtitle'] = items['زیرنویس']
        banners['type'] = items['نوع_id']
        media = {}
        if (banner[i].شناسه_بنر.حذف == 0):
            media['image'] = banner[i].شناسه_بنر.فایل.name
            media['caption']=banner[i].شناسه_بنر.توضیح
            media['title'] = banner[i].شناسه_بنر.عنوان
            media['alt'] = banner[i].شناسه_بنر.جایگزین
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


    ### TODO:later ###
