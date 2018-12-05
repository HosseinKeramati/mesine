from django.shortcuts import render

# Create your views here.
from jalali_date import datetime2jalali, date2jalali

def my_view(request):
     jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')
