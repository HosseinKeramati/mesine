from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from mesineapp.models import *
import json

def banner(request):

    banner = بنر.objects.filter(نوع_id = 2 , حذف = 0).select_related('شناسه_بنر')
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

def news_card(request):
    if(request.body):
        body = json.loads(request.body.decode('utf-8'))
        id=body['id']
        news_card_list=[]
        if(خبر.objects.filter(شناسه = id)):
            card = خبر.objects.filter(شناسه = id, حذف = 0).select_related('شناسه_عکس')
            cat=list(card.values())
            i=0
            for objects in cat:
                info={}
                info['id'] = cat[i]['شناسه']
                info['title'] = cat[i]['عنوان_خبر']
                info['text'] = cat[i]['شرح_خبر']
                info['marketing_text'] = cat[i]['متن_مارکتینگ']
                info['helping_parameter'] = cat[i]['پارامتر_کمکی']
                info['alt'] = cat[i]['جایگزین']
                media = {}
                if objects['شناسه_عکس_id']:
                    if (card[i].شناسه_عکس.حذف == 0 ):
                        card_info={}
                        card_info['id'] = card[i].شناسه_عکس.شناسه
                        card_info['file'] = card[i].شناسه_عکس.فایل.name
                        card_info['description'] = card[i].شناسه_عکس.توضیح
                        card_info['title'] = card[i].شناسه_عکس.عنوان
                        card_info['alt'] = card[i].شناسه_عکس.جایگزین
                        news_card_list.append({
                        'news_info' : info,
                        'news_card' :card_info
                        })
                        i=i+1
                else:
                    news_card_list.append({
                    'news_info' : info,
                    'news_card' : None
                    })
                    i=i+1
            result = {
            "ok" : True,
            "status_code": 200,
            "result": news_card_list
            }
        elif(body['limit']!=0):
            news_slider_list=[]
            limit=body['limit']
            offset=0
            if(body['offset'] != 0 ):
                offset = body['offset']
            card = خبر.objects.filter( حذف = 0).select_related('شناسه_عکس')[offset:limit]
            cat=list(card.values())

            i=0
            for objects in cat:
                info={}
                info['id'] = cat[i]['شناسه']
                info['title'] = cat[i]['عنوان_خبر']
                info['text'] = cat[i]['شرح_خبر']
                info['marketing_text'] = cat[i]['متن_مارکتینگ']
                info['helping_parameter'] = cat[i]['پارامتر_کمکی']
                info['alt'] = cat[i]['جایگزین']
                media = {}
                if objects['شناسه_عکس_id']:
                    if (card[i].شناسه_عکس.حذف == 0 ):
                        card_info={}
                        card_info['id'] = card[i].شناسه_عکس.شناسه
                        card_info['file'] = card[i].شناسه_عکس.فایل.name
                        card_info['description'] = card[i].شناسه_عکس.توضیح
                        card_info['title'] = card[i].شناسه_عکس.عنوان
                        card_info['alt'] = card[i].شناسه_عکس.جایگزین
                        news_card_list.append({
                        'news_info' : info,
                        'news_card' :card_info
                        })
                        i=i+1
                else:
                    news_card_list.append({
                    'news_info' : info,
                    'news_card' : None
                    })
                    i=i+1
            result = {
            "ok" : True,
            "status_code": 200,
            "result": news_card_list
            }
    else:
        news_card_list=[]
        card =خبر.objects.filter(حذف = 0).select_related('شناسه_عکس')
        cat=list(card.values())
        i=0
        for objects in cat:
            info={}
            info['id'] = cat[i]['شناسه']
            info['title'] = cat[i]['عنوان_خبر']
            info['text'] = cat[i]['شرح_خبر']
            info['marketing_text'] = cat[i]['متن_مارکتینگ']
            info['helping_parameter'] = cat[i]['پارامتر_کمکی']
            info['alt'] = cat[i]['جایگزین']
            media = {}
            if objects['شناسه_عکس_id']:
                if (card[i].شناسه_عکس.حذف == 0 ):
                    card_info={}
                    card_info['id'] = card[i].شناسه_عکس.شناسه
                    card_info['file'] = card[i].شناسه_عکس.فایل.name
                    card_info['description'] = card[i].شناسه_عکس.توضیح
                    card_info['title'] = card[i].شناسه_عکس.عنوان
                    card_info['alt'] = card[i].شناسه_عکس.جایگزین
                    news_card_list.append({
                    'news_info' : info,
                    'news_card' :card_info
                    })
                    i=i+1
            else:
                news_card_list.append({
                'news_info' : info,
                'news_card' : None
                })
                i=i+1
    result = {
    "ok" : True,
    "status_code": 200,
    "result": news_card_list
    }


    return JsonResponse(result,json_dumps_params={'indent': 2},safe=False)

def news_content(request):
    if(request.body):
        body = json.loads(request.body.decode('utf-8'))
        if(body['id'] != 0):
            id=body['id']
            news_list=[]
            media = خبر.objects.filter(شناسه = id , حذف = 0).select_related('شناسه_عکس')
            marketing = خبر.objects.filter(شناسه = id , حذف = 0).select_related('شناسه_عکس_مارکتینگ')
            cat=list(media.values())
            i=0
            for objects in cat:
                slider_list={}
                media_list={}
                card_list={}
                info={}
                info['id'] = cat[i]['شناسه']
                info['title'] = cat[i]['عنوان_خبر']
                info['text'] = cat[i]['شرح_خبر']
                info['marketing_text'] = cat[i]['متن_مارکتینگ']
                info['helping_parameter'] = cat[i]['پارامتر_کمکی']
                info['alt'] = cat[i]['جایگزین']
                card_info = {}
                print(objects)
                if objects['شناسه_عکس_id']:
                    if (media[i].شناسه_عکس.حذف == 0 ):
                        card_info['id'] = media[i].شناسه_عکس.شناسه
                        card_info['file'] = media[i].شناسه_عکس.فایل.name
                        card_info['description'] = media[i].شناسه_عکس.توضیح
                        card_info['title'] = media[i].شناسه_عکس.عنوان
                        card_info['alt'] = media[i].شناسه_عکس.جایگزین
                        card_list['news_pic'] = card_info
                else:
                    card_list['news_pic'] = None
                slider_info = {}
                if objects['شناسه_عکس_مارکتینگ_id']:
                    if (objects['شناسه_عکس_مارکتینگ_id'] == marketing[i].شناسه_عکس_مارکتینگ.شناسه and marketing[i].شناسه_عکس_مارکتینگ.حذف == 0 ):
                        slider_info['id'] = marketing[i].شناسه_عکس_مارکتینگ.شناسه
                        slider_info['file'] = marketing[i].شناسه_عکس_مارکتینگ.فایل.name
                        slider_info['description'] = marketing[i].شناسه_عکس_مارکتینگ.توضیح
                        slider_info['title'] = marketing[i].شناسه_عکس_مارکتینگ.عنوان
                        slider_info['alt'] = marketing[i].شناسه_عکس_مارکتینگ.جایگزین
                        slider_list['marketing_pic'] = slider_info
                        i=i+1

                else:
                    slider_list['marketing_pic'] = None
                    i=i+1
                news_list.append({
                'info' : info,
                'news_pic' : card_list,
                'marketing_pic' : slider_list
                })
            result = {
            "ok" : True,
            "status_code": 200,
            "result": news_list
            }
        elif(body['limit']!=0):
            news_list=[]
            limit=body['limit']
            offset=0
            if(body['offset'] != 0 ):
                offset = body['offset']
            media = خبر.objects.filter( حذف = 0).select_related('شناسه_عکس')[offset:limit]
            marketing = خبر.objects.filter( حذف = 0).select_related('شناسه_عکس_مارکتینگ')[offset:limit]
            cat=list(media.values())

            i=0
            for objects in cat:
                slider_list={}
                media_list={}
                card_list={}
                info={}
                info['id'] = cat[i]['شناسه']
                info['title'] = cat[i]['عنوان_خبر']
                info['text'] = cat[i]['شرح_خبر']
                info['marketing_text'] = cat[i]['متن_مارکتینگ']
                info['helping_parameter'] = cat[i]['پارامتر_کمکی']
                info['alt'] = cat[i]['جایگزین']
                card_info = {}
                print(objects)
                if objects['شناسه_عکس_id']:
                    if (media[i].شناسه_عکس.حذف == 0 ):
                        card_info['id'] = media[i].شناسه_عکس.شناسه
                        card_info['file'] = media[i].شناسه_عکس.فایل.name
                        card_info['description'] = media[i].شناسه_عکس.توضیح
                        card_info['title'] = media[i].شناسه_عکس.عنوان
                        card_info['alt'] = media[i].شناسه_عکس.جایگزین
                        card_list['news_pic'] = card_info
                else:
                    card_list['news_pic'] = None
                slider_info = {}
                if objects['شناسه_عکس_مارکتینگ_id']:
                    if (objects['شناسه_عکس_مارکتینگ_id'] == marketing[i].شناسه_عکس_مارکتینگ.شناسه and marketing[i].شناسه_عکس_مارکتینگ.حذف == 0 ):
                        slider_info['id'] = marketing[i].شناسه_عکس_مارکتینگ.شناسه
                        slider_info['file'] = marketing[i].شناسه_عکس_مارکتینگ.فایل.name
                        slider_info['description'] = marketing[i].شناسه_عکس_مارکتینگ.توضیح
                        slider_info['title'] = marketing[i].شناسه_عکس_مارکتینگ.عنوان
                        slider_info['alt'] = marketing[i].شناسه_عکس_مارکتینگ.جایگزین
                        slider_list['marketing_pic'] = slider_info
                        i=i+1

                else:
                    slider_list['marketing_pic'] = None
                    i=i+1

                news_list.append({
                'info' : info,
                'news_pic' : card_list,
                'marketing_pic' : slider_list
                })
            result = {
            "ok" : True,
            "status_code": 200,
            "result": news_list
            }

    else:
        news_list=[]

        media = خبر.objects.filter( حذف = 0).select_related('شناسه_عکس')
        marketing = خبر.objects.filter( حذف = 0).select_related('شناسه_عکس_مارکتینگ')
        cat=list(media.values())
        i=0
        for objects in cat:
            slider_list={}
            media_list={}
            card_list={}
            info={}
            info['id'] = cat[i]['شناسه']
            info['title'] = cat[i]['عنوان_خبر']
            info['text'] = cat[i]['شرح_خبر']
            info['marketing_text'] = cat[i]['متن_مارکتینگ']
            info['helping_parameter'] = cat[i]['پارامتر_کمکی']
            info['alt'] = cat[i]['جایگزین']
            card_info = {}
            print(objects)
            if objects['شناسه_عکس_id']:
                if (media[i].شناسه_عکس.حذف == 0 ):
                    card_info['id'] = media[i].شناسه_عکس.شناسه
                    card_info['file'] = media[i].شناسه_عکس.فایل.name
                    card_info['description'] = media[i].شناسه_عکس.توضیح
                    card_info['title'] = media[i].شناسه_عکس.عنوان
                    card_info['alt'] = media[i].شناسه_عکس.جایگزین
                    card_list['news_card'] = card_info
            else:
                card_list['news_card'] = None
            slider_info = {}
            if objects['شناسه_عکس_مارکتینگ_id']:
                if (objects['شناسه_عکس_مارکتینگ_id'] == marketing[i].شناسه_عکس_مارکتینگ.شناسه and marketing[i].شناسه_عکس_مارکتینگ.حذف == 0 ):
                    slider_info['id'] = marketing[i].شناسه_عکس_مارکتینگ.شناسه
                    slider_info['file'] = marketing[i].شناسه_عکس_مارکتینگ.فایل.name
                    slider_info['description'] = marketing[i].شناسه_عکس_مارکتینگ.توضیح
                    slider_info['title'] = marketing[i].شناسه_عکس_مارکتینگ.عنوان
                    slider_info['alt'] = marketing[i].شناسه_عکس_مارکتینگ.جایگزین
                    slider_list['news_slider'] = slider_info
                    i=i+1

            else:
                slider_list['news_slider'] = None
                i=i+1
            news_list.append({
            'info' : info,
            'news_pic' : card_list,
            'marketing_pic' : slider_list
            })
        sorted(media_list,reverse=False)
        result = {
        "ok" : True,
        "status_code": 200,
        "result": news_list
        }
    return JsonResponse(result,json_dumps_params={'indent': 2},safe=False)

def news_search(request):
    if(request.body):
        body = json.loads(request.body.decode('utf-8'))
        if(body['limit']==0):
            if(body['search_key']!=0):
                target=body['search_key']

                news=خبر.objects.filter(حذف = 0)


                news_ids=[]
                i=0
                for objects in list(news.values()):
                    news_id={}


                    if target in list(news.values())[i]['عنوان_خبر']:
                        news_id['title_news_id']=objects['شناسه']
                    if target in list(news.values())[i]['شرح_خبر']:
                        news_id['text_news_id']=objects['شناسه']
                    if news_id:
                        news_ids.append(news_id)
                    i=i+1

                result={
                "result" : news_ids
                }

            else:

                news=خبر.objects.filter( حذف = 0)



                news_ids=[]
                i=0
                for objects in list(news.values()):
                    news_id={}

                    news_id['id'] = objects['شناسه']
                    if news_id:
                        news_ids.append(news_id)
                    i=i+1


                result={
                "result" : news_ids
                }


        elif(body['limit'] != 0):
            limit=body['limit']
            offset=0
            if(body['offset'] != 0):
                offset = body['offset']
            if(body['search_key']):
                target=body['search_key']
                news=خبر.objects.filter(حذف = 0)



                news_ids=[]
                i=0
                for objects in list(news.values()):
                    news_id={}
                    if target in list(news.values())[i]['عنوان_خبر']:
                        news_id['title_news_id']=objects['شناسه']
                    if target in list(news.values())[i]['شرح_خبر']:
                        news_id['text_news_id']=objects['شناسه']
                    if news_id:
                        news_ids.append(news_id)
                    i=i+1


                result={
                "result" : news_ids[offset:limit]
                }

            else:
                result = {
                "ok" : False,
                "status_code": 400,
                "result": "Search Key did\'nt pass! "
                }

        else:
            pass





    else:
        result = {
        "ok" : False,
        "status_code": 400,
        "result": "Needs inputs in JSON format! "
        }
    return JsonResponse(result,json_dumps_params={'indent': 2},safe=False)
