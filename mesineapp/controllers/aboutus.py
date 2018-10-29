from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from mesineapp.models import *
import json


def banner(request):

    banner = بنر.objects.filter(نوع_id = 4 , حذف = 0).select_related('شناسه_بنر')
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


def about_us(request):

    ax = درباره_ما.objects.filter(حذف = 0).select_related('عکس۱')
    ax2 = درباره_ما.objects.filter(حذف = 0).select_related('عکس۲')
    banner_list=[]
    ban =list(ax.values())
    i=0
    for items in ban:
        banners={}
        banners['id'] = items['شناسه']
        banners['text']=items['متن']
        banners['alt'] = items['جایگزین']
        media = {}
        media2 = {}
        if (ax[i].عکس۱.حذف == 0 and ax2[i].عکس۲.حذف == 0):
            media['image'] = ax[i].عکس۱.فایل.name
            media['caption']=ax[i].عکس۱.توضیح
            media['title'] = ax[i].عکس۱.عنوان
            media['alt'] = ax[i].عکس۱.جایگزین

            media2['image'] = ax2[i].عکس۲.فایل.name
            media2['caption']=ax2[i].عکس۲.توضیح
            media2['title'] = ax2[i].عکس۲.عنوان
            media2['alt'] = ax2[i].عکس۲.جایگزین

            banner_list.append({
            'media1' : media,
            'media2' : media2,
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
