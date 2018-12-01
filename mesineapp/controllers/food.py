from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from mesineapp.models import *
import json





def foods_slider(request):
    print(request)
    if(request.body):
        body = json.loads(request.body.decode('utf-8'))
        id=body["id"]
        foods_slider_list=[]
        m = Media.objects.filter(title__contains = 'foods slider')
        media=list(m.values())
        print("media :",media)
        for objects in media:
            if(objects['deleted'] == 0):
                news_s={}
                media = {}
                if (objects['id'] == items['media_id_id']):
                    media['image'] = objects['file']
                    media['caption']=objects['description']
                    media['title'] = objects['title']
                    media['alt'] = objects['alt']
                    foods_slider_list.append({
                    'media' : media
                    })
        result = {
        "ok" : True,
        "status_code": 200,
        "result": foods_slider_list
        }
    else:
        foods_slider_list=[]
        m = Media.objects.filter(title__contains = 'news slider')
        media=list(m.values())
        print("media :",media)
        for objects in media:
            if(objects['deleted'] == 0):
                news_s={}
                media = {}
                if (objects['id'] == items['media_id_id']):
                    media['image'] = objects['file']
                    media['caption']=objects['description']
                    media['title'] = objects['title']
                    media['alt'] = objects['alt']
                    foods_slider_list.append({
                    'media' : media
                    })
        result = {
        "ok" : True,
        "status_code": 200,
        "result": news_slider_list
        }
    print("result : ",result)
    return JsonResponse(result,json_dumps_params={'indent': 2},safe=False)

def foods_card(request):
    if(request.body):
        body = json.loads(request.body.decode('utf-8'))
        id=body["id"]
        print("id :" , id)
        foods_card_list=[]
        m = Media.objects.filter(title__contains = 'foods card')
        media=list(m.values())
        print("media :",media)
        print("media :",media)
        for objects in media:
            if(objects['deleted'] == 0):
                media = {}
                if (objects['id'] == items['media_id_id']):
                    media['image'] = objects['file']
                    media['caption']=objects['description']
                    media['title'] = objects['title']
                    media['alt'] = objects['alt']
                    foods_card_list.append({
                    'media' : media
                    })
    # if (banners["title"] == "homepage"):
        # news_card_list.append(news_c)
        result = {
        "ok" : True,
        "status_code": 200,
        "result": foods_card_list
        }

    else:
        result ={
        "ok" : False,
        "Error" : "id didn\'t passed"
        }
    print("result : ",result)
    return JsonResponse(result,json_dumps_params={'indent': 2},safe=False)

def foods_content(request):
    if(request.body):
        body = json.loads(request.body.decode('utf-8'))
        print("BODY :" , body)
        if(body["id"] !=0):
            id=body["id"]
            foods_contents = []
            Social_network = []
            m = Media.objects.filter(title__contains = 'foods content')
            Midia=list(m.values())
            nc=Food.objects.filter(id = id)
            for items in list(nc.values()):
                print("stat : " ,str(items["deleted"]));
                if(items['deleted'] == 0):
                    news_c={}
                    news_c['title']=items["title"]
                    news_c['html text'] = items['text']
                    # news_c['news category'] = items['foods_category_id']
                    print("HEEEEERRRR : " ,news_c)
                    if items['media_id_id']:

                        for objects in Midia:
                            media = {}
                            if (objects['id'] == items['media_id_id']):
                                media['image'] = objects['file']
                                media['caption']=objects['description']
                                media['title'] = objects['title']
                                media['alt'] = objects['alt']
                                foods_contents.append({
                                'media' : media,
                                'info' : news_c,
                                })
                                social=Social_network_content.objects.all()
                                for types in list(social.values()):
                                    if(types['deleted'] == 0):
                                        social_net = {}
                                        social_net['text'] = types['text']
                                        b = types['type_id']
                                        c = Social_network_type.objects.filter(id = b)
                                        print(c)
                                        f= list(c.values())
                                        print('F :' ,f)
                                        social_net['type'] = f[0]['text']
                                        Social_network.append(social_net)
                    else:
                        print("ELSE")
                        foods_contents.append({
                        'info' : news_c,
                        'media' : {},
                        })

            result = {
            "ok" : True,
            "status_code": 200,
            "result": news_contents,
            "social network" :Social_network
            }
            return JsonResponse(result,json_dumps_params={'indent': 2},safe=False)
        elif(body["limit"] != 0):
            print("ELSE IF RUNING")
            limit = body["limit"]
            offset=0
            if(body["offset"] != 0):
                offset=body["offset"]
            foods_contents = []
            Social_network = []
            m = Media.objects.filter(title__contains = 'foods content')
            Midia=list(m.values())
            nc=Food.objects.all()[offset:limit]
            print("media :",Midia)
            # print("nc :" , list(nc.values()))
            for items in list(nc.values()):
                print("stat : " ,str(items["deleted"]));
                if(items['deleted'] == 0):
                    news_c={}
                    news_c['title']=items["title"]
                    news_c['html text'] = items['text']
                    # news_c['news category'] = items['news_category_id']
                    print("HEEEEERRRR : " ,news_c)
                    if items['media_id_id']:
                        for objects in Midia:
                            media = {}
                            if (objects['id'] == items['media_id_id']):
                                media['image'] = objects['file']
                                media['caption']=objects['description']
                                media['title'] = objects['title']
                                media['alt'] = objects['alt']
                                foods_contents.append({
                                'media' : media,
                                'info' : news_c,
                                })
                                social=Social_network_content.objects.all()
                                for types in list(social.values()):
                                    if(types['deleted'] == 0):
                                        social_net = {}
                                        social_net['text'] = types['text']
                                        b = types['type_id']
                                        c = Social_network_type.objects.filter(id = b)
                                        print(c)
                                        f= list(c.values())
                                        print('F :' ,f)
                                        social_net['type'] = f[0]['text']
                                        Social_network.append(social_net)

                    else:
                        print("ELSE")
                        foods_contents.append({
                        'info' : news_c,
                        'media' : {},
                        })
            result = {
            "ok" : True,
            "status_code": 200,
            "result": foods_contents,
            "social network" :Social_network
            }
            return JsonResponse(result,json_dumps_params={'indent': 2},safe=False)

    else:
        foods_contents = []
        Social_network = []
        m = Media.objects.filter(title__contains = 'foods content')
        Midia=list(m.values())
        nc=Food.objects.all()
        print("media :",Midia)
        # print("nc :" , list(nc.values()))
        for items in list(nc.values()):
            print("stat : " ,items['media_id_id']);
            # print("ID : " , id(items['media_id_id']))
            if(items['deleted'] == 0):
                news_c={}
                news_c['title']=items["title"]
                news_c['html text'] = items['text']
                # news_c['news category'] = items['news_category_id']
                # print("HEEEEERRRR : " ,news_c)
                # print(type(items['media_id_id']))
                if items['media_id_id']:
                    print("IF")
                    for objects in Midia:
                        media = {}
                        if (objects['id'] == items['media_id_id']):
                            media['image'] = objects['file']
                            media['caption']=objects['description']
                            media['title'] = objects['title']
                            media['alt'] = objects['alt']
                            foods_contents.append({
                            'info' : news_c,
                            'media' : media,
                            })
                            social=Social_network_content.objects.all()
                            for types in list(social.values()):
                                if(types['deleted'] == 0):
                                    social_net = {}
                                    social_net['text'] = types['text']
                                    b = types['type_id']
                                    c = Social_network_type.objects.filter(id = b)
                                    print(c)
                                    f= list(c.values())
                                    print('F :' ,f)
                                    social_net['type'] = f[0]['text']
                                    Social_network.append(social_net)
                else:
                    print("ELSE")
                    foods_contents.append({
                    'info' : news_c,
                    'media' : {},
                    })

        result = {
        "ok" : True,
        "status_code": 200,
        "result": foods_contents,
        "social network" :Social_network
        }

        return JsonResponse(result,json_dumps_params={'indent': 2},safe=False)

# def news_category(request):
#     if(request.body):
#         body = json.loads(request.body.decode('utf-8'))
#         if(body["id"] != 0):
#             id=body["id"]
#             news_category_list =[]
#             ncc=News_category.objects.filter(id = id)
#             m = Media.objects.filter(title__contains = 'news category')
#             Midia=list(m.values())
#             for items in list(ncc.values()):
#                 ncc_ob={}
#                 if(items['deleted'] == 0):
#                     ncc_ob['text']=items['text']
#                     ncc_ob['media_id'] = items['media_id_id']
#                     for objects in Midia:
#                         media = {}
#                         if (objects['id'] == items['media_id_id']):
#                             media['image'] = objects['file']
#                             media['caption']=objects['description']
#                             media['title'] = objects['title']
#                             media['alt'] = objects['alt']
#                             news_category_list.append({
#                             'media' : media,
#                             'info' : ncc_ob,
#                             })
#
#             result = {
#             "ok" : True,
#             "status_code": 200,
#             "result": news_category_list
#             }
#         elif(body["limit"] != 0):
#             limit=body["limit"]
#             offset=0
#             if(body["offset"] != 0):
#                 offset=body["offset"]
#             news_category_list =[]
#             ncc=News_category.objects.all()[offset:limit]
#             m = Media.objects.filter(title__contains = 'news category')
#             Midia=list(m.values())
#             for items in list(ncc.values()):
#                 ncc_ob={}
#                 if(items['deleted'] == 0):
#                     ncc_ob['text']=items['text']
#                     ncc_ob['media_id'] = items['media_id_id']
#                     for objects in Midia:
#                         media = {}
#                         if (objects['id'] == items['media_id_id']):
#                             media['image'] = objects['file']
#                             media['caption']=objects['description']
#                             media['title'] = objects['title']
#                             media['alt'] = objects['alt']
#                             news_category_list.append({
#                             'media' : media,
#                             'info' : ncc_ob,
#                             })
#
#             result = {
#             "ok" : True,
#             "status_code": 200,
#             "result": news_category_list
#             }
#     else:
#         news_category_list =[]
#         ncc=News_category.objects.all()
#         m = Media.objects.filter(title__contains = 'news category')
#         Midia=list(m.values())
#         for items in list(ncc.values()):
#             ncc_ob={}
#             if(items['deleted'] == 0):
#                 ncc_ob['text']=items['text']
#                 ncc_ob['media_id'] = items['media_id_id']
#                 for objects in Midia:
#                     media = {}
#                     if (objects['id'] == items['media_id_id']):
#                         media['image'] = objects['file']
#                         media['caption']=objects['description']
#                         media['title'] = objects['title']
#                         media['alt'] = objects['alt']
#                         news_category_list.append({
#                         'media' : media,
#                         'info' : ncc_ob,
#                         })
#
#         result = {
#         "ok" : True,
#         "status_code": 200,
#         "result": news_category_list
#         }
#
#     return JsonResponse(result,json_dumps_params={'indent': 2},safe=False)
#
#س def news_category_news(request):
#     if(request.body):
#         body = json.loads(request.body.decode('utf-8'))
#         if(body["id"] != 0):
#             id=body["id"]
#             news_category_news_list =[]
#             nccn=News_category_new.objects.filter(id = id)
#             for items in list(nccn.values()):
#                 nccn_ob={}
#                 if(items['deleted'] == 0):
#                     news=New.objects.filter(id = items['news_id_id'])
#                     news_cat=News_category.objects.filter(id = items['news_category_id_id'])
#                     n=list(news.values())
#                     ncat=list(news_cat.values())
#
#                     nccn_ob['news_id']=items['news_id_id']
#                     nccn_ob['news_title']=n[0]['title']
#                     nccn_ob['news_text']=n[0]['text']
#                     nccn_ob['news_media_id']=n[0]["media_id_id"]
#                     nccn_ob['news_category'] = n[0]['news_category_id']
#                     nccn_ob['news_category_id'] = items['news_category_id_id']
#                     nccn_ob['news_category_text']=n[0]['text']
#                     nccn_ob['news_category_media_id']=n[0]["media_id_id"]
#
#                     news_category_news_list.append(nccn_ob)
#
#             result = {
#             "ok" : True,
#             "status_code": 200,
#             "result": news_category_news_list
#             }
#         elif(body["limit"] != 0):
#             offset=0
#             limit=body["limit"]
#             if(body["offset"] != 0):
#                 offset=body["offset"]
#             news_category_news_list =[]
#             nccn=News_category_new.objects.all()[offset:limit]
#             for items in list(nccn.values()):
#                 nccn_ob={}
#                 if(items['deleted'] == 0):
#                     news=New.objects.filter(id = items['news_id_id'])
#                     news_cat=News_category.objects.filter(id = items['news_category_id_id'])
#                     n=list(news.values())
#                     ncat=list(news_cat.values())
#
#                     nccn_ob['news_id']=items['news_id_id']
#                     nccn_ob['news_title']=n[0]['title']
#                     nccn_ob['news_text']=n[0]['text']
#                     nccn_ob['news_media_id']=n[0]["media_id_id"]
#                     nccn_ob['news_category'] = n[0]['news_category_id']
#                     nccn_ob['news_category_id'] = items['news_category_id_id']
#                     nccn_ob['news_category_text']=n[0]['text']
#                     nccn_ob['news_category_media_id']=n[0]["media_id_id"]
#                     news_category_news_list.append(nccn_ob)
#
#             result = {
#             "ok" : True,
#             "status_code": 200,
#             "result": news_category_news_list
#             }
#     else:
#         news_category_news_list =[]
#         nccn=News_category_new.objects.all()
#         for items in list(nccn.values()):
#             nccn_ob={}
#             if(items['deleted'] == 0):
#                 news=New.objects.filter(id = items['news_id_id'])
#                 news_cat=News_category.objects.filter(id = items['news_category_id_id'])
#                 n=list(news.values())
#                 ncat=list(news_cat.values())
#
#                 nccn_ob['news_id']=items['news_id_id']
#                 nccn_ob['news_title']=n[0]['title']
#                 nccn_ob['news_text']=n[0]['text']
#                 nccn_ob['news_media_id']=n[0]["media_id_id"]
#                 nccn_ob['news_category'] = n[0]['news_category_id']
#                 nccn_ob['news_category_id'] = items['news_category_id_id']
#                 nccn_ob['news_category_text']=n[0]['text']
#                 nccn_ob['news_category_media_id']=n[0]["media_id_id"]
#
#                 news_category_news_list.append(nccn_ob)
#
#         result = {
#         "ok" : True,
#         "status_code": 200,
#         "result": news_category_news_list
#         }
#     return JsonResponse(result,json_dumps_params={'indent': 2},safe=False)
