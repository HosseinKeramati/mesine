from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from mesineapp.models import *
import json

def collection_slider(request):
    if(request.body):
        body = json.loads(request.body.decode('utf-8'))
        if(body["id"] != 0):
            id=body["id"]
            collection_slider_list=[]
            slider = Main_category.objects.filter(id = id, deleted = 0).select_related('slider')
            cat=list(slider.values())
            i=0
            print("media :",cat)
            # info={}
            # info["title"] = cat[0]['title']
            # info["subtitle"] = cat[0]["subtitle"]
            for objects in cat:
            #     s=Media.objects.filter(id = objects["banner_id_id"])
            #     items=list(s.values())
            #     V=Banner.objects.filter(id = objects['card_id'])
            #     c_card=list(v.values())
            #     card_info = {}
            #     if (objects['card_id'] == c_card[0]['id'] and c_card[0]['deleted'] == 0 ):
            #         card_info['title'] = c_card[0]['title']
            #         card_info['subtitle'] = c_card[0]['subtitle']
            #         card_info['card_id'] = c_card[0]['banner_id_id']
            #         card_info['type'] = c_card[0]['type']
            #         collection_slider_list.append({
            #         'card' :card_info
            #         })
            #     else:
            #         collection_slider_list.append({
            #         'card' : 'deleted'
            #         })
                # z=Banner.objects.filter(id = cat[0]['slider_id'])
                # c_slider=list(z.values())
                slider_info = {}
                info={}
                info["id"]=objects["id"]
                info["title"]=objects["title"]
                info["subtitle"]=objects["subtitle"]
                info["helping_parameter"]=objects["helping_parameter"]
                # print("slider: ",c_slider)
                if objects['slider_id']:
                    if (slider[i].slider.deleted == 0 ):
                        slider_info['id'] = slider[i].slider.id
                        slider_info['file'] = slider[i].slider.file.name
                        slider_info['description'] = slider[i].slider.description
                        slider_info['title'] = slider[i].slider.title
                        slider_info['alt'] = slider[i].slider.alt
                        collection_slider_list.append({
                        "collection_info" : info,
                        'collection_slider' :slider_info
                        })
                        i=i+1
                else:
                    collection_slider_list.append({
                    "collection_info" : info,
                    'collection_slider' : None
                    })
                    i=i+1
            # collec_s={}


                # media = {}
                # if (objects['banner_id_id'] == items[0]['id'] and items[0]['deleted'] == 0 ):
                #     media['image'] = items[0]['file']
                #     media['caption'] = items[0]['description']
                #     media['title'] = items[0]['title']
                #     media['alt'] = items[0]['alt']
                #     collection_slider_list.append({
                #     'info' : info,
                #     'media' : media
                #     })
                # else:
                #     collection_slider_list.append({
                #     'info' : info,
                #     'media' : 'deleted'
                #     })
        # if (banners["title"] == "homepage"):
            # collection_slider_list.append(collec_s)
            result = {
            "ok" : True,
            "status_code": 200,
            "result": collection_slider_list
            }
        elif(body["limit"]!=0):
            collection_slider_list=[]
            limit=body["limit"]
            offset=0
            if(body["offset"] != 0 ):
                offset = body["offset"]
            slider = Main_category.objects.filter( deleted = 0).select_related('slider')[offset:limit]
            cat=list(slider.values())
            print("media :",cat)
            # info={}
            # info["title"] = cat[0]['title']
            # info["subtitle"] = cat[0]["subtitle"]
            i=0
            for objects in cat:
            #     s=Media.objects.filter(id = objects["banner_id_id"])
            #     items=list(s.values())
            #     V=Banner.objects.filter(id = objects['card_id'])
            #     c_card=list(v.values())
            #     card_info = {}
            #     if (objects['card_id'] == c_card[0]['id'] and c_card[0]['deleted'] == 0 ):
            #         card_info['title'] = c_card[0]['title']
            #         card_info['subtitle'] = c_card[0]['subtitle']
            #         card_info['card_id'] = c_card[0]['banner_id_id']
            #         card_info['type'] = c_card[0]['type']
            #         collection_slider_list.append({
            #         'card' :card_info
            #         })
            #     else:
            #         collection_slider_list.append({
            #         'card' : 'deleted'
            #         })
                # z=Banner.objects.filter(id = cat[0]['slider_id'])
                # c_slider=list(z.values())
                slider_info = {}
                info={}
                info["id"]=objects["id"]
                info["title"]=objects["title"]
                info["subtitle"]=objects["subtitle"]
                info["helping_parameter"]=objects["helping_parameter"]
                if objects['slider_id']:
                    if (slider[i].slider.deleted == 0 ):
                        slider_info['file'] = slider[i].slider.file.name
                        slider_info['description'] = slider[i].slider.description
                        slider_info['title'] = slider[i].slider.title
                        slider_info['alt'] = slider[i].slider.alt
                        collection_slider_list.append({
                        "collection_info" : info,
                        'collection_slider' :slider_info
                        })
                        i=i+1
                else:
                    collection_slider_list.append({
                    "collection_info" : info,
                    'collection_slider' : None
                    })
                    i=i+1
            # collec_s={}


                # media = {}
                # if (objects['banner_id_id'] == items[0]['id'] and items[0]['deleted'] == 0 ):
                #     media['image'] = items[0]['file']
                #     media['caption'] = items[0]['description']
                #     media['title'] = items[0]['title']
                #     media['alt'] = items[0]['alt']
                #     collection_slider_list.append({
                #     'info' : info,
                #     'media' : media
                #     })
                # else:
                #     collection_slider_list.append({
                #     'info' : info,
                #     'media' : 'deleted'
                #     })
        # if (banners["title"] == "homepage"):
            # collection_slider_list.append(collec_s)
            result = {
            "ok" : True,
            "status_code": 200,
            "result": collection_slider_list
            }

    else:
        collection_slider_list=[]
        slider = Main_category.objects.filter( deleted = 0).select_related('slider')
        cat=list(slider.values())
        print("media :",cat)
        # info={}
        # info["title"] = cat[0]['title']
        # info["subtitle"] = cat[0]["subtitle"]
        i=0
        for objects in cat:
        #     s=Media.objects.filter(id = objects["banner_id_id"])
        #     items=list(s.values())
        #     V=Banner.objects.filter(id = objects['card_id'])
        #     c_card=list(v.values())
        #     card_info = {}
        #     if (objects['card_id'] == c_card[0]['id'] and c_card[0]['deleted'] == 0 ):
        #         card_info['title'] = c_card[0]['title']
        #         card_info['subtitle'] = c_card[0]['subtitle']
        #         card_info['card_id'] = c_card[0]['banner_id_id']
        #         card_info['type'] = c_card[0]['type']
        #         collection_slider_list.append({
        #         'card' :card_info
        #         })
        #     else:
        #         collection_slider_list.append({
        #         'card' : 'deleted'
        #         })
            # z=Banner.objects.filter(id = objects['slider_id'])
            # c_slider=list(z.values())
            # print("slider: ",c_slider)
            slider_info = {}
            info={}
            info["id"]=objects["id"]
            info["title"]=objects["title"]
            info["subtitle"]=objects["subtitle"]
            info["helping_parameter"]=objects["helping_parameter"]
            if objects['slider_id']:
                if (slider[i].slider.deleted == 0 ):
                    slider_info['id'] = slider[i].slider.id
                    slider_info['file'] = slider[i].slider.file.name
                    slider_info['description'] = slider[i].slider.description
                    slider_info['title'] = slider[i].slider.title
                    slider_info['alt'] = slider[i].slider.alt
                    collection_slider_list.append({
                    "collection_info" : info,
                    'collection_slider' :slider_info
                    })
                    i=i+1
            else:
                collection_slider_list.append({
                "collection_info" : info,
                'collection_slider' : None
                })
                i=i+1
        # collec_s={}


            # media = {}
            # if (objects['banner_id_id'] == items[0]['id'] and items[0]['deleted'] == 0 ):
            #     media['image'] = items[0]['file']
            #     media['caption'] = items[0]['description']
            #     media['title'] = items[0]['title']
            #     media['alt'] = items[0]['alt']
            #     collection_slider_list.append({
            #     'info' : info,
            #     'media' : media
            #     })
            # else:
            #     collection_slider_list.append({
            #     'info' : info,
            #     'media' : 'deleted'
            #     })
    # if (banners["title"] == "homepage"):
        # collection_slider_list.append(collec_s)
        result = {
        "ok" : True,
        "status_code": 200,
        "result": collection_slider_list
        }

    print("result : ",result)
    return JsonResponse(result,json_dumps_params={'indent': 2},safe=False)


def collection_card(request):
    if(request.body):
        body = json.loads(request.body.decode('utf-8'))
        if(body["id"] != 0):
            id=body["id"]
            collection_card_list=[]
            card = Main_category.objects.filter(id = id, deleted = 0).select_related('card')
            cat=list(card.values())
            print("media :",cat)
            # info={}
            # info["title"] = cat[0]['title']
            # info["subtitle"] = cat[0]["subtitle"]
            i=0
            for objects in cat:
            #     s=Media.objects.filter(id = objects["banner_id_id"])
            #     items=list(s.values())
            #     V=Banner.objects.filter(id = objects['card_id'])
            #     c_card=list(v.values())
            #     card_info = {}
            #     if (objects['card_id'] == c_card[0]['id'] and c_card[0]['deleted'] == 0 ):
            #         card_info['title'] = c_card[0]['title']
            #         card_info['subtitle'] = c_card[0]['subtitle']
            #         card_info['card_id'] = c_card[0]['banner_id_id']
            #         card_info['type'] = c_card[0]['type']
            #         collection_slider_list.append({
            #         'card' :card_info
            #         })
            #     else:
            #         collection_slider_list.append({
            #         'card' : 'deleted'
            #         })
                # z=Banner.objects.filter(id = cat[0]['card_id'])
                # c_card=list(z.values())
                card_info = {}
                info={}
                info["id"]=objects["id"]
                info["title"]=objects["title"]
                info["subtitle"]=objects["subtitle"]
                info["helping_parameter"]=objects["helping_parameter"]
                # print("slider: ",c_card)
                if objects['card_id']:
                    if (card[i].card.deleted == 0 ):
                        card_info['id'] = card[i].card.id
                        card_info['file'] = card[i].card.file.name
                        card_info['description'] = card[i].card.description
                        card_info['title'] = card[i].card.title
                        card_info['alt'] = card[i].card.alt
                        collection_card_list.append({
                        "card_info" : info,
                        'collection_card' :card_info
                        })
                        i=i+1
                else:
                    collection_card_list.append({
                    "card_info" : info,
                    'collection_card' : None
                    })
                    i=i+1
            # collec_s={}


                # media = {}
                # if (objects['banner_id_id'] == items[0]['id'] and items[0]['deleted'] == 0 ):
                #     media['image'] = items[0]['file']
                #     media['caption'] = items[0]['description']
                #     media['title'] = items[0]['title']
                #     media['alt'] = items[0]['alt']
                #     collection_slider_list.append({
                #     'info' : info,
                #     'media' : media
                #     })
                # else:
                #     collection_slider_list.append({
                #     'info' : info,
                #     'media' : 'deleted'
                #     })
        # if (banners["title"] == "homepage"):
            # collection_slider_list.append(collec_s)
            result = {
            "ok" : True,
            "status_code": 200,
            "result": collection_card_list
            }
        elif(body["limit"]!=0):
            collection_card_list=[]
            limit=body["limit"]
            offset=0
            if(body["offset"] != 0 ):
                offset = body["offset"]
            card = Main_category.objects.filter(deleted = 0).select_related('card')[offset:limit]
            cat=list(card.values())
            print("media :",cat)
            # info={}
            # info["title"] = cat[0]['title']
            # info["subtitle"] = cat[0]["subtitle"]
            i=0
            for objects in cat:
            #     s=Media.objects.filter(id = objects["banner_id_id"])
            #     items=list(s.values())
            #     V=Banner.objects.filter(id = objects['card_id'])
            #     c_card=list(v.values())
            #     card_info = {}
            #     if (objects['card_id'] == c_card[0]['id'] and c_card[0]['deleted'] == 0 ):
            #         card_info['title'] = c_card[0]['title']
            #         card_info['subtitle'] = c_card[0]['subtitle']
            #         card_info['card_id'] = c_card[0]['banner_id_id']
            #         card_info['type'] = c_card[0]['type']
            #         collection_slider_list.append({
            #         'card' :card_info
            #         })
            #     else:
            #         collection_slider_list.append({
            #         'card' : 'deleted'
            #         })
                # z=Banner.objects.filter(id = cat[0]['card_id'])
                # c_card=list(z.values())
                card_info = {}
                info={}
                info["title"]=objects["title"]
                info["subtitle"]=objects["subtitle"]
                info["helping_parameter"]=objects["helping_parameter"]
                if objects['card_id']:
                    if (card[i].card.deleted == 0 ):
                        card_info['id'] = card[i].card.id
                        card_info['file'] = card[i].card.file.name
                        card_info['description'] = card[i].card.description
                        card_info['title'] = card[i].card.title
                        card_info['alt'] = card[i].card.alt
                        collection_card_list.append({
                        "card_info" : info,
                        'collection_card' :card_info
                        })
                        i=i+1
                else:
                    collection_card_list.append({
                    "card_info" : info,
                    'collection_card' : None
                    })
                    i=i+1
            # collec_s={}


                # media = {}
                # if (objects['banner_id_id'] == items[0]['id'] and items[0]['deleted'] == 0 ):
                #     media['image'] = items[0]['file']
                #     media['caption'] = items[0]['description']
                #     media['title'] = items[0]['title']
                #     media['alt'] = items[0]['alt']
                #     collection_slider_list.append({
                #     'info' : info,
                #     'media' : media
                #     })
                # else:
                #     collection_slider_list.append({
                #     'info' : info,
                #     'media' : 'deleted'
                #     })
        # if (banners["title"] == "homepage"):
            # collection_slider_list.append(collec_s)
            result = {
            "ok" : True,
            "status_code": 200,
            "result": collection_card_list
            }

    else:
        collection_card_list=[]
        card = Main_category.objects.filter(deleted = 0).select_related('card')
        cat=list(card.values())
        print("media :",cat)
        # info={}
        # info["title"] = cat[0]['title']
        # info["subtitle"] = cat[0]["subtitle"]
        i=0
        for objects in cat:
        #     s=Media.objects.filter(id = objects["banner_id_id"])
        #     items=list(s.values())
        #     V=Banner.objects.filter(id = objects['card_id'])
        #     c_card=list(v.values())
        #     card_info = {}
        #     if (objects['card_id'] == c_card[0]['id'] and c_card[0]['deleted'] == 0 ):
        #         card_info['title'] = c_card[0]['title']
        #         card_info['subtitle'] = c_card[0]['subtitle']
        #         card_info['card_id'] = c_card[0]['banner_id_id']
        #         card_info['type'] = c_card[0]['type']
        #         collection_slider_list.append({
        #         'card' :card_info
        #         })
        #     else:
        #         collection_slider_list.append({
        #         'card' : 'deleted'
        #         })
            # z=Banner.objects.filter(id = objects['card_id'])
            # c_card=list(z.values())
            # print("card: ",c_card)
            card_info = {}
            info={}
            info["id"]=objects["id"]
            info["title"]=objects["title"]
            info["subtitle"]=objects["subtitle"]
            info["helping_parameter"]=objects["helping_parameter"]
            if objects['card_id']:
                if (card[i].card.deleted == 0 ):
                    card_info['id'] = card[i].card.id
                    card_info['file'] = card[i].card.file.name
                    card_info['description'] = card[i].card.description
                    card_info['title'] = card[i].card.title
                    card_info['alt'] = card[i].card.alt
                    collection_card_list.append({
                    "card_info" : info,
                    'collection_card' :card_info
                    })
                    i=i+1
            else:
                collection_card_list.append({
                "card_info" : info,
                'collection_card' : None
                })
                i=i+1
        # collec_s={}


            # media = {}
            # if (objects['banner_id_id'] == items[0]['id'] and items[0]['deleted'] == 0 ):
            #     media['image'] = items[0]['file']
            #     media['caption'] = items[0]['description']
            #     media['title'] = items[0]['title']
            #     media['alt'] = items[0]['alt']
            #     collection_slider_list.append({
            #     'info' : info,
            #     'media' : media
            #     })
            # else:
            #     collection_slider_list.append({
            #     'info' : info,
            #     'media' : 'deleted'
            #     })
    # if (banners["title"] == "homepage"):
        # collection_slider_list.append(collec_s)
        result = {
        "ok" : True,
        "status_code": 200,
        "result": collection_card_list
        }

    print("result : ",result)
    return JsonResponse(result,json_dumps_params={'indent': 2},safe=False)


def collection_content(request):
    if(request.body):
        body = json.loads(request.body.decode('utf-8'))
        if(body["id"] != 0):
            id=body["id"]
            collection_list=[]
            media = Main_category.objects.filter(id=id, deleted = 0).select_related('media_id')
            slider = Main_category.objects.filter(id=id, deleted = 0).select_related('slider')
            card = Main_category.objects.filter(id=id, deleted = 0).select_related('card')
            cat=list(media.values())
            print("media :",cat)
            i=0
            for objects in cat:
                slider_list={}
                media_list={}
                card_list={}
                print("objects" , objects)
                info={}
                info["id"]=objects["id"]
                info["title"]=objects["title"]
                info["subtitle"]=objects["subtitle"]
                info["helping_parameter"]=objects["helping_parameter"]
                # s=Media.objects.filter(id = objects["media_id_id"])
                # items=list(s.values())
                # v=Banner.objects.filter(id = objects['card_id'])
                # c_card=list(v.values())
                card_info = {}
                if objects['card_id']:
                    if (card[i].card.deleted == 0 ):
                        card_info['id'] = card[i].card.id
                        card_info['file'] = card[i].card.file.name
                        card_info['description'] = card[i].card.description
                        card_info['title'] = card[i].card.title
                        card_info['alt'] = card[i].card.alt
                        card_list['collection_card'] = card_info
                else:
                    card_list['collection_card'] = None
                # z=Banner.objects.filter(id = cat[0]['slider_id'])
                # c_slider=list(z.values())
                slider_info = {}
                # print("slider: ",c_slider)

                if objects['slider_id']:
                    if (objects['slider_id'] == slider[i].slider.id and slider[i].slider.deleted == 0 ):
                        slider_info['id'] = slider[i].slider.id
                        slider_info['file'] = slider[i].slider.file.name
                        slider_info['description'] = slider[i].slider.description
                        slider_info['title'] = slider[i].slider.title
                        slider_info['alt'] = slider[i].slider.alt
                        slider_list['collection_slider'] = slider_info

                else:
                    slider_list['collection_slider'] = None

            # collec_s={}


                media_info= {}
                if objects['media_id_id']:
                    if (media[i].media_id.deleted == 0 ):
                        media_info['id'] = media[i].media_id.id
                        media_info['file'] = media[i].media_id.file.name
                        media_info['description'] = media[i].media_id.description
                        media_info['title'] = media[i].media_id.title
                        media_info['alt'] = media[i].media_id.alt
                        media_list['collection_media'] = media_info
                        i=i+1
                else:
                    media_list['collection_media'] = None
                    i=i+1
        # if (banners["title"] == "homepage"):
            # collection_slider_list.append(collec_s)
                collection_list.append({
                "info" : info,
                'card' : card_list,
                'slider' : slider_list,
                'media' : media_list
                })
            result = {
            "ok" : True,
            "status_code": 200,
            "result": collection_list
            }
        elif(body["limit"]!=0):
            collection_list=[]
            limit=body["limit"]
            offset=0
            if(body["offset"] != 0 ):
                offset = body["offset"]
            media = Main_category.objects.filter( deleted = 0).select_related('media_id')[offset:limit]
            slider = Main_category.objects.filter( deleted = 0).select_related('slider')[offset:limit]
            card = Main_category.objects.filter( deleted = 0).select_related('card')[offset:limit]
            cat=list(media.values())
            print("media :",cat)
            i=0
            for objects in cat:
                slider_list={}
                media_list={}
                card_list={}
                print("objects" , objects)
                info={}
                info["id"]=objects["id"]
                info["title"]=objects["title"]
                info["subtitle"]=objects["subtitle"]
                info["helping_parameter"]=objects["helping_parameter"]
                # s=Media.objects.filter(id = objects["media_id_id"])
                # items=list(s.values())
                # v=Banner.objects.filter(id = objects['card_id'])
                # c_card=list(v.values())
                card_info = {}
                if objects['card_id']:
                    if (card[i].card.deleted == 0 ):
                        card_info['id'] = card[i].card.id
                        card_info['file'] = card[i].card.file.name
                        card_info['description'] = card[i].card.description
                        card_info['title'] = card[i].card.title
                        card_info['alt'] = card[i].card.alt
                        card_list['collection_card'] = card_info
                else:
                    card_list['collection_card'] = None
                # z=Banner.objects.filter(id = cat[0]['slider_id'])
                # c_slider=list(z.values())
                slider_info = {}
                # print("slider: ",c_slider)

                if objects['slider_id']:
                    if (objects['slider_id'] == slider[i].slider.id and slider[i].slider.deleted == 0 ):
                        slider_info['id'] = slider[i].slider.id
                        slider_info['file'] = slider[i].slider.file.name
                        slider_info['description'] = slider[i].slider.description
                        slider_info['title'] = slider[i].slider.title
                        slider_info['alt'] = slider[i].slider.alt
                        slider_list['collection_slider'] = slider_info

                else:
                    slider_list['collection_slider'] = None

            # collec_s={}


                media_info= {}
                if objects['media_id_id']:
                    if (media[i].media_id.deleted == 0 ):
                        media_info['id'] = media[i].media_id.id
                        media_info['file'] = media[i].media_id.file.name
                        media_info['description'] = media[i].media_id.description
                        media_info['title'] = media[i].media_id.title
                        media_info['alt'] = media[i].media_id.alt
                        media_list['collection_media'] = media_info
                        i=i+1
                else:
                    media_list['collection_media'] = None
                    i=i+1
        # if (banners["title"] == "homepage"):
            # collection_slider_list.append(collec_s)
                collection_list.append({
                "info" : info,
                'card' : card_list,
                'slider' : slider_list,
                'media' : media_list
                })
            result = {
            "ok" : True,
            "status_code": 200,
            "result": collection_list
            }

    else:
        collection_list=[]

        media = Main_category.objects.filter( deleted = 0).select_related('media_id')
        slider = Main_category.objects.filter( deleted = 0).select_related('slider')
        card = Main_category.objects.filter( deleted = 0).select_related('card')
        cat=list(media.values())
        print("media :",cat)
        i=0
        for objects in cat:
            slider_list={}
            media_list={}
            card_list={}
            print("objects" , objects)
            info={}
            info["id"]=objects["id"]
            info["title"]=objects["title"]
            info["subtitle"]=objects["subtitle"]
            info["helping_parameter"]=objects["helping_parameter"]
            # s=Media.objects.filter(id = objects["media_id_id"])
            # items=list(s.values())
            # v=Banner.objects.filter(id = objects['card_id'])
            # c_card=list(v.values())
            card_info = {}
            if objects['card_id']:
                if (card[i].card.deleted == 0 ):
                    card_info['id'] = card[i].card.id
                    card_info['file'] = card[i].card.file.name
                    card_info['description'] = card[i].card.description
                    card_info['title'] = card[i].card.title
                    card_info['alt'] = card[i].card.alt
                    card_list['collection_card'] = card_info
            else:
                card_list['collection_card'] = None
            # z=Banner.objects.filter(id = cat[0]['slider_id'])
            # c_slider=list(z.values())
            slider_info = {}
            # print("slider: ",c_slider)

            if objects['slider_id']:
                if (objects['slider_id'] == slider[i].slider.id and slider[i].slider.deleted == 0 ):
                    slider_info['id'] = slider[i].slider.id
                    slider_info['file'] = slider[i].slider.file.name
                    slider_info['description'] = slider[i].slider.description
                    slider_info['title'] = slider[i].slider.title
                    slider_info['alt'] = slider[i].slider.alt
                    slider_list['collection_slider'] = slider_info

            else:
                slider_list['collection_slider'] = None

        # collec_s={}


            media_info= {}
            if objects['media_id_id']:
                if (media[i].media_id.deleted == 0 ):
                    media_info['id'] = media[i].media_id.id
                    media_info['file'] = media[i].media_id.file.name
                    media_info['description'] = media[i].media_id.description
                    media_info['title'] = media[i].media_id.title
                    media_info['alt'] = media[i].media_id.alt
                    media_list['collection_media'] = media_info
                    i=i+1
            else:
                media_list['collection_media'] = None
                i=i+1
    # if (banners["title"] == "homepage"):
        # collection_slider_list.append(collec_s)
            collection_list.append({
            "info" : info,
            'card' : card_list,
            'slider' : slider_list,
            'media' : media_list
            })
        result = {
        "ok" : True,
        "status_code": 200,
        "result": collection_list
        }

    print("result : ",result)
    return JsonResponse(result,json_dumps_params={'indent': 2},safe=False)

def collection_search(request):
    if(request.body):
        body = json.loads(request.body.decode('utf-8'))
        if(body["limit"]==0):
            if(body["search_key"]!=0):
                target=body["search_key"]
                collection=Main_category.objects.filter( deleted = 0)



                news_ids=[]
                i=0
                for objects in list(collection.values()):
                    news_id={}
                    print(target)
                    # print(list(news.values()))
                    # matches = filter(,list(news.values()))
                    if target in list(collection.values())[i]["title"]:
                        news_id["title_collection_id"]=objects["id"]
                    if target in list(collection.values())[i]["subtitle"]:
                        news_id["subtitle_collection_id"]=objects["id"]
                    if news_id:
                        news_ids.append(news_id)
                    i=i+1
                    print(objects)

                result={
                "result" : news_ids
                }

                # else:
                #     news=New.objects.filter(deleted = 0)
                #     print(type(New))
                #
                #     news_ids=[]
                #     i=0
                #     for objects in list(news.values()):
                #         news_id={}
                #         print(target)
                #         print(list(news.values()))
                #         # matches = filter(,list(news.values()))
                #         if target in list(news.values())[i]["title"]:
                #             news_id["title_news_id"]=objects["id"]
                #         if target in list(news.values())[i]["text"]:
                #             news_id["text_news_id"]=objects["id"]
                #         news_ids.append(news_id)
                #         i=i+1
                #         print(objects)
                #
                #     result={
                #     "result" : news_ids
                #     }

            else:
                result = {
                "ok" : False,
                "status_code": 400,
                "result": "Search Key did\'nt pass! "
                }
        elif(body["limit"] != 0):
            limit=body["limit"]
            offset=0
            if(body["offset"] != 0):
                offset = body["offset"]
            if(body["search_key"]):
                target=body["search_key"]
                collection=Main_category.objects.filter( deleted = 0)
                print(type(New))
                news_ids=[]
                i=0
                for objects in list(collection.values()):
                    news_id={}
                    print(target)
                    print(list(collection.values()))
                    # matches = filter(,list(news.values()))
                    if target in list(collection.values())[i]["title"]:
                        news_id["title_collection_id"]=objects["id"]
                    if target in list(collection.values())[i]["subtitle"]:
                        news_id["subtitle_collection_id"]=objects["id"]
                    if news_id:
                        news_ids.append(news_id)
                    i=i+1
                    print(objects)

                result={
                "result" : news_ids[offset:limit]
                }
                # else:
                #     news=New.objects.filter(deleted = 0)
                #     print(type(New))
                #
                #     news_ids=[]
                #     i=0
                #     for objects in list(news.values()):
                #         news_id={}
                #         print(target)
                #         print(list(news.values()))
                #         # matches = filter(,list(news.values()))
                #         if target in list(news.values())[i]["title"]:
                #             news_id["title_news_id"]=objects["id"]
                #         if target in list(news.values())[i]["text"]:
                #             news_id["text_news_id"]=objects["id"]
                #         news_ids.append(news_id)
                #         i=i+1
                #         print(objects)
                #
                #     result={
                #     "result" : news_ids[offset:limit]
                #     }

            else:
                result = {
                "ok" : False,
                "status_code": 400,
                "result": "Search Key did\'nt pass! "
                }






    else:
        result = {
        "ok" : False,
        "status_code": 400,
        "result": "Needs inputs in JSON format! "
        }
    return JsonResponse(result,json_dumps_params={'indent': 2},safe=False)
