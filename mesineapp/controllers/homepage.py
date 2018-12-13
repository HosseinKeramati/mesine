#encoding=utf-8

from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from mesineapp.models import *
import json

def services(request):

    service = سرویس.objects.filter(حذف = 0).select_related('شناسه_عکس')
    banner_list=[]
    ban =list(service.values())
    i=0
    for items in ban:
        services={}
        services['id'] = items['شناسه']
        services['title']=items['عنوان']
        services['subtitle'] = items['زیرنویس']
        services['helping_parameter'] = items['پارامتر_کمکی']
        services['alt'] = items['جایگزین']
        media = {}
        if (service[i].شناسه_عکس.حذف == 0):
            media['image'] = service[i].شناسه_عکس.فایل.name
            media['caption']=service[i].شناسه_عکس.توضیح
            media['title'] = service[i].شناسه_عکس.عنوان
            media['alt'] = service[i].شناسه_عکس.جایگزین
            banner_list.append({
            'media' : media,
            'banner_info' : services
            })
            i=i+1
        else:
            banner_list.append({
            'media' : "Null or deleted",
            'banner_info' : services
            })
            i=i+1
    result = {
    "ok" : True,
    "status_code": 200,
    "result":banner_list
    }
    return JsonResponse(result,json_dumps_params={'indent': 2},safe=False)


def favorite(request):

    favorite = منوی_محبوب_رستوران.objects.filter(حذف = 0).select_related('عنوان_غذا')
    banner_list=[]
    ban =list(favorite.values())
    i=0
    for items in ban:
        banners={}
        banners['id'] = items['شناسه']
        media = {}
        if (favorite[i].عنوان_غذا.حذف == 0):
            print(ban)
            x = رسانه.objects.filter(حذف = 0 , شناسه =ban[i]['شناسه'])
            print(x.values())
            media['image'] = x[0].فایل.name
            media['caption']=x[0].توضیح
            media['title'] = favorite[i].عنوان_غذا.عنوان
            media['alt'] = x[0].جایگزین
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




def banner(request):

    banner = بنر.objects.filter(نوع_id = 1 , حذف = 0).select_related('شناسه_بنر')
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

# def assist_company(request):
#     logo = Logo.objects.filter(deleted = 0).select_related('logo_id')
#     assist_company_list=[]
#     i=0
#     for items in list(logo.values()):
#         assist_company_o = {}
#         assist_company_o['link'] = items['text']
#         media = {}
#         if (logo[i].logo_id.deleted == 0):
#             media['logo'] = logo[i].logo_id.file
#             media['caption']=logo[i].logo_id.description
#             media['title'] = logo[i].logo_id.title
#             media['alt'] = logo[i].logo_id.alt
#             assist_company_list.append({
#             'media' : media,
#             'logo_info' : assist_company_o
#             })
#             i=i+1
#         else:
#             assist_company_list.append({
#             'media' : "Null or deleted",
#             'logo_info' : assist_company_o
#             })
#             i=i+1
#     result = {
#     "ok" : True,
#     "status_code": 200,
#     "result": assist_company_list
#     }
#
#     result = json.dumps(result, ensure_ascii=False)
#
#     return JsonResponse(result,json_dumps_params={'indent': 2},safe=False,)
#
def value_proposition(request):
    value = ارزش_های_پیشنهادی.objects.filter(حذف = 0).select_related('شناسه_عکس')
    value_proposition_list = []
    i=0
    for items in list(value.values()):
        valu_ob = {}
        valu_ob['propose_value'] = items['ارزش_پیشنهادی']
        media = {}
        if (value[i].شناسه_عکس.حذف == 0):
            media['image'] = value[i].شناسه_عکس.فایل.name
            media['caption']=value[i].شناسه_عکس.توضیح
            media['title'] = value[i].شناسه_عکس.عنوان
            media['alt'] = value[i].شناسه_عکس.جایگزین
            value_proposition_list.append({
            'media': media,
            'value_proposition_info': valu_ob
            })
            i=i+1
        else:
            value_proposition_list.append({
            'media': "deleted" ,
            'valu_proposition_info': valu_ob
            })
            i=i+1

                # value_proposition_list.append(valu_ob)
    result = {
    "ok" : True,
    "status_code": 200,
    "result": value_proposition_list
    }
    return JsonResponse(result,json_dumps_params={'indent': 2},safe=False)

#
# def other_program(request):
#     other_p = Other_program.objects.filter(deleted = 0).select_related('media_id')
#     other_program_list = []
#     i=0
#     for items in list(other_p.values()):
#         other_p_ob = {}
#         other_p_ob['caption'] =items['text']
#         media = {}
#         if (other_p[i].media_id.deleted == 0):
#             media['logo'] = other_p[i].media_id.file.name
#             media['caption']=other_p[i].media_id.description
#             media['title'] = other_p[i].media_id.title
#             media['alt'] = other_p[i].media_id.alt
#             other_program_list.append({
#             'media' : media,
#             'other_program_info' : other_p_ob
#             })
#             i=i+1
#         else:
#             other_program_list.append({
#             'media' : "deleted",
#             'other_program_info' : other_p_ob
#             })
#             i=i+1
#     result = {
#     "ok" : True,
#     "status_code": 200,
#     "result": other_program_list
#     }
#     return JsonResponse(result,json_dumps_params={'indent': 2},safe=False)
