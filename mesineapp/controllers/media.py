from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from mesineapp.models import *
import json


def media_analyzer(request):
    if(request.body):
        medix={}
        body = json.loads(request.body.decode('utf-8'))
        id=body["id"]
        if(رسانه.objects.filter(شناسه = id)):
            media=رسانه.objects.filter(شناسه = id)
            m=list(media.values())
            medi={}
            medi['file'] = m[0]['فایل']
            medi['description'] = m[0]['توضیح']
            medi['title'] = m[0]['عنوان']
            medi['alt'] = m[0]['جایگزین']

            result = {
            "ok" : True,
            "status_code": 200,
            "result": medi
            }
            return JsonResponse(result,json_dumps_params={'indent': 2},safe=False)


        else:
            result = {
            "ok" : False,
            "status_code": 404,
            "result": "Media-id didn\'t found !!"
            }
            return JsonResponse(result,json_dumps_params={'indent': 2},safe=False)
    else:
        result = {
        "ok" : False,
        "status_code": 400,
        "result": "Media-id didn\'t passed!!"
        }
        return JsonResponse(result,json_dumps_params={'indent': 2},safe=False)
