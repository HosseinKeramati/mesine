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


def main_course(request):
    food_list=[]
    media = منوی_غذا.objects.filter( حذف = 0 , دسته_بندی_غذا_id = 1).select_related('شناسه_عکس')
    cat=list(media.values())
    i=0
    for objects in cat:
        slider_list={}
        media_list={}
        card_list={}
        info={}
        info['id'] = cat[i]['شناسه']
        info['title'] = cat[i]['عنوان']
        info['content'] = cat[i]['محتویات']
        card_info = {}
        if objects['شناسه_عکس_id']:
            if (media[i].شناسه_عکس.حذف == 0 ):
                card_info['id'] = media[i].شناسه_عکس.شناسه
                card_info['file'] = media[i].شناسه_عکس.فایل.name
                card_info['description'] = media[i].شناسه_عکس.توضیح
                card_info['title'] = media[i].شناسه_عکس.عنوان
                card_info['alt'] = media[i].شناسه_عکس.جایگزین
                card_list['news_card'] = card_info
                i=i+1
        else:
            card_list['news_card'] = None
            i=i+1

        food_list.append({
        'info' : info,
        'food_pic' : card_list,
        })
    result = {
    "ok" : True,
    "status_code": 200,
    "result": food_list
    }
    return JsonResponse(result,json_dumps_params={'indent': 2},safe=False)


def starter(request):
    food_list=[]
    media = منوی_غذا.objects.filter( حذف = 0 , دسته_بندی_غذا_id = 2).select_related('شناسه_عکس')
    cat=list(media.values())
    i=0
    for objects in cat:
        slider_list={}
        media_list={}
        card_list={}
        info={}
        info['id'] = cat[i]['شناسه']
        info['title'] = cat[i]['عنوان']
        info['content'] = cat[i]['محتویات']
        card_info = {}
        if objects['شناسه_عکس_id']:
            if (media[i].شناسه_عکس.حذف == 0 ):
                card_info['id'] = media[i].شناسه_عکس.شناسه
                card_info['file'] = media[i].شناسه_عکس.فایل.name
                card_info['description'] = media[i].شناسه_عکس.توضیح
                card_info['title'] = media[i].شناسه_عکس.عنوان
                card_info['alt'] = media[i].شناسه_عکس.جایگزین
                card_list['news_card'] = card_info
                i=i+1
        else:
            card_list['news_card'] = None
            i=i+1

        food_list.append({
        'info' : info,
        'food_pic' : card_list,
        })
    result = {
    "ok" : True,
    "status_code": 200,
    "result": food_list
    }
    return JsonResponse(result,json_dumps_params={'indent': 2},safe=False)


def drinks(request):
    food_list=[]
    media = منوی_غذا.objects.filter( حذف = 0 , دسته_بندی_غذا_id = 3).select_related('شناسه_عکس')
    cat=list(media.values())
    i=0
    for objects in cat:
        slider_list={}
        media_list={}
        card_list={}
        info={}
        info['id'] = cat[i]['شناسه']
        info['title'] = cat[i]['عنوان']
        info['content'] = cat[i]['محتویات']
        card_info = {}
        if objects['شناسه_عکس_id']:
            if (media[i].شناسه_عکس.حذف == 0 ):
                card_info['id'] = media[i].شناسه_عکس.شناسه
                card_info['file'] = media[i].شناسه_عکس.فایل.name
                card_info['description'] = media[i].شناسه_عکس.توضیح
                card_info['title'] = media[i].شناسه_عکس.عنوان
                card_info['alt'] = media[i].شناسه_عکس.جایگزین
                card_list['news_card'] = card_info
                i=i+1
        else:
            card_list['news_card'] = None
            i=i+1

        food_list.append({
        'info' : info,
        'food_pic' : card_list,
        })
    result = {
    "ok" : True,
    "status_code": 200,
    "result": food_list
    }
    return JsonResponse(result,json_dumps_params={'indent': 2},safe=False)

def salads(request):
    food_list=[]
    media = منوی_غذا.objects.filter( حذف = 0 , دسته_بندی_غذا_id = 4).select_related('شناسه_عکس')
    cat=list(media.values())
    i=0
    for objects in cat:
        slider_list={}
        media_list={}
        card_list={}
        info={}
        info['id'] = cat[i]['شناسه']
        info['title'] = cat[i]['عنوان']
        info['content'] = cat[i]['محتویات']
        card_info = {}
        if objects['شناسه_عکس_id']:
            if (media[i].شناسه_عکس.حذف == 0 ):
                card_info['id'] = media[i].شناسه_عکس.شناسه
                card_info['file'] = media[i].شناسه_عکس.فایل.name
                card_info['description'] = media[i].شناسه_عکس.توضیح
                card_info['title'] = media[i].شناسه_عکس.عنوان
                card_info['alt'] = media[i].شناسه_عکس.جایگزین
                card_list['news_card'] = card_info
                i=i+1
        else:
            card_list['news_card'] = None
            i=i+1

        food_list.append({
        'info' : info,
        'food_pic' : card_list,
        })
    result = {
    "ok" : True,
    "status_code": 200,
    "result": food_list
    }
    return JsonResponse(result,json_dumps_params={'indent': 2},safe=False)

def dessert(request):
    food_list=[]
    media = منوی_غذا.objects.filter( حذف = 0 , دسته_بندی_غذا_id = 5).select_related('شناسه_عکس')
    cat=list(media.values())
    i=0
    for objects in cat:
        slider_list={}
        media_list={}
        card_list={}
        info={}
        info['id'] = cat[i]['شناسه']
        info['title'] = cat[i]['عنوان']
        info['content'] = cat[i]['محتویات']
        card_info = {}
        if objects['شناسه_عکس_id']:
            if (media[i].شناسه_عکس.حذف == 0 ):
                card_info['id'] = media[i].شناسه_عکس.شناسه
                card_info['file'] = media[i].شناسه_عکس.فایل.name
                card_info['description'] = media[i].شناسه_عکس.توضیح
                card_info['title'] = media[i].شناسه_عکس.عنوان
                card_info['alt'] = media[i].شناسه_عکس.جایگزین
                card_list['news_card'] = card_info
                i=i+1
        else:
            card_list['news_card'] = None
            i=i+1

        food_list.append({
        'info' : info,
        'food_pic' : card_list,
        })
    result = {
    "ok" : True,
    "status_code": 200,
    "result": food_list
    }
    return JsonResponse(result,json_dumps_params={'indent': 2},safe=False)
