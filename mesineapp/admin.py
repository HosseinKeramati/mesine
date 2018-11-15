from django.contrib import admin
from mesineapp.models import *
# register your models hereself.
from django.contrib.auth.models import User, Group
from jet.admin import CompactInline
from django.utils.translation import ugettext_lazy as _
from jet.dashboard import modules
from jet.dashboard.dashboard import Dashboard, AppIndexDashboard

# admin.site.unregister(User)
# admin.site.unregister(Group)


class Pro(admin.ModelAdmin):
    list_display = ( 'شناسه', 'فایل', 'عنوان' ,'حذف',)
    list_filter = ('عنوان',)
    search_fields = ('عنوان',)
    prepopulated_fields = {}     #dictionary needed for seo


class PP(admin.ModelAdmin):
    list_display = ('شناسه', 'نوع' ,'حذف',)
    list_filter = ('نوع',)
    search_fields = ('نوع',)
    prepopulated_fields = {}     #dictionary needed for seo

class PQ(admin.ModelAdmin):
    list_display = ('شناسه', 'متن' ,'حذف',)
    list_filter = ('متن',)
    search_fields = ('متن',)
    prepopulated_fields = {}     #dictionary needed for seo

admin.site.site_header = "مدیریت رستوران مسینه"
admin.site.site_title = "پورتال مدیریت رستوران مسینه"
admin.site.index_title = "به پورتال مدیریت رستوران مسینه خوش آمدید."


admin.site.register(رسانه,Pro)
admin.site.register(ارزش_های_پیشنهادی)
# admin.site.register(User_type)
# admin.site.register(User)
admin.site.register(منوی_محبوب_رستوران)
admin.site.register(نوع_شبکه_اجتماعی , PQ)
admin.site.register(خبر)
admin.site.register(نوع_عکس , PP)
admin.site.register(بنر)
admin.site.register(سرویس)
admin.site.register(لوگو)
admin.site.register(پانویس)
admin.site.register(سربرگ)
admin.site.register(منوی_غذا)
admin.site.register(درباره_ما)
admin.site.register(تماس_با_ما)
admin.site.register(شبکه_اجتماعی)
