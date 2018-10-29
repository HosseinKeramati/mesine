from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from mesineapp.models import *


def footer(request):

    footer = پانویس.objects.filter(حذف = 0)
    banner_list=[]
    ban =list(footer.values())
    for items in ban:
        banners={}
        banners['id'] = items['شناسه']
        banners['text']=items['متن']
        banners['link'] = items['لینک']
        banner_list.append({
        'footer' : banners
        })
    result = {
    "ok" : True,
    "status_code": 200,
    "result":banner_list
    }
    return JsonResponse(result,json_dumps_params={'indent': 2},safe=False)
