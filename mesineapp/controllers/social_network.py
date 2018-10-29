from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from mesineapp.models import *
import json

# Create your views here.

def social_network_type(request):
    social_network = نوع_شبکه_اجتماعی.objects.filter(حذف = 0)
    banner_list=[]
    ban =list(social_network.values())
    for items in ban:
        banners={}
        banners['id'] = items['شناسه']
        banners['text']=items['متن']
        banner_list.append({
        'social_network_type' : banners
        })
    result = {
    "ok" : True,
    "status_code": 200,
    "result":banner_list
    }
    return JsonResponse(result,json_dumps_params={'indent': 2},safe=False)

def social_network(request):
    social_network = شبکه_اجتماعی.objects.filter(حذف = 0)
    banner_list=[]
    ban =list(social_network.values())
    print(ban)
    for items in ban:
        banners={}
        banners['id'] = items['شناسه']
        banners['username']=items['نام_کاربری']
        if(items['نوع_شبکه_اجتماعی_id'] == 1):
            banners['link']= "instagram.com/" + items['نام_کاربری']
        if(items['نوع_شبکه_اجتماعی_id'] == 2):
            banners['link']= "telegram.me/" + items['نام_کاربری']
        banner_list.append({
        'social_network' : banners
        })
    result = {
    "ok" : True,
    "status_code": 200,
    "result":banner_list
    }
    return JsonResponse(result,json_dumps_params={'indent': 2},safe=False)
