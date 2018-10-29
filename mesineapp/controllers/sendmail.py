from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from mesineapp.models import *
import json


def email(request):
    print(request)
    body = json.loads(request.body.decode('utf-8'))
    user_mail = body["email"]
    sender = 'Sender : ' + user_mail +' \n\n'
    subject = body["title"]
    message = sender + "Message: \n\n" + body["content"]
    email_from = 'messineh.resturant@gmail.com'
    recipient_list = ["keramati_hossein@ae.sharif.edu",]
    send_mail( subject, message, email_from, recipient_list )

    result = {
    "ok" : True,
    "status_code": 200,
    }

    return JsonResponse(result,json_dumps_params={'indent': 2},safe=False)
