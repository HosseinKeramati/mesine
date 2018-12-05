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


class Pp(admin.ModelAdmin):
    list_display = ('شناسه', 'نوع' ,'حذف',)
    list_filter = ('نوع',)
    search_fields = ('نوع',)
    prepopulated_fields = {}     #dictionary needed for seo

class Pq(admin.ModelAdmin):
    list_display = ('شناسه', 'متن' ,'حذف',)
    list_filter = ('متن',)
    search_fields = ('متن',)
    prepopulated_fields = {}     #dictionary needed for seo

class Val(admin.ModelAdmin):
    list_display = ('شناسه','ارزش_پیشنهادی' ,'حذف',)
    list_filter = ('ارزش_پیشنهادی',)
    search_fields = ('ارزش_پیشنهادی',)
    prepopulated_fields = {}     #dictionary needed for seo

class Ne(admin.ModelAdmin):
    list_display = ('شناسه','عنوان_خبر' , 'تاریخ' ,'ساعت' ,'حذف',)
    list_filter = ('عنوان_خبر' , 'تاریخ' ,)
    search_fields = ('عنوان_خبر',)
    prepopulated_fields = {}     #dictionary needed for seo

class Ban(admin.ModelAdmin):
    list_display = ('شناسه' , 'عنوان' , 'حذف' ,)
    list_filter = ('عنوان',)
    search_fields = ('عنوان',)
    prepopulated_fields = {}     #dictionary needed for seo

class Lo(admin.ModelAdmin):
    list_display = ('شناسه' , 'متن' , 'حذف',)
    list_filter = ('متن' ,)
    search_fields = ('متن',)
    prepopulated_fields = {}     #dictionary needed for seo


class Ty(admin.ModelAdmin):
    list_display = ('شناسه' , 'نوع' ,)
    list_filter = ('نوع' ,)
    search_fields = ('نوع',)
    prepopulated_fields = {}     #dictionary needed for seo

class Fo(admin.ModelAdmin):
    list_display = ('شناسه' , 'عنوان' , 'دسته_بندی_غذا', 'حذف' ,)
    list_filter = ('دسته_بندی_غذا', 'عنوان' ,)
    search_fields = ('عنوان', 'دسته_بندی_غذا' ,)
    prepopulated_fields = {}     #dictionary needed for seo

class Ab(admin.ModelAdmin):
    list_display = ('شناسه' , 'حذف',)
    list_filter = ('حذف' ,)
    search_fields = ('حذف',)
    prepopulated_fields = {}     #dictionary needed for seo

class Me(admin.ModelAdmin):
    list_display = ('شناسه' , 'عنوان_غذا', 'حذف' ,)
    list_filter = ('عنوان_غذا',)
    search_fields = ('عنوان_غذا',)
    prepopulated_fields = {}     #dictionary needed for seo

class So(admin.ModelAdmin):
    list_display = ('شناسه' , 'نام_کاربری', 'نوع_شبکه_اجتماعی','حذف',)
    list_filter = ('نام_کاربری' ,)
    search_fields = ('نام_کاربری',)
    prepopulated_fields = {}     #dictionary needed for seo

admin.site.site_header = "مدیریت رستوران مسینه"
admin.site.site_title = "پورتال مدیریت رستوران مسینه"
admin.site.index_title = "به پورتال مدیریت رستوران مسینه خوش آمدید."


admin.site.register(رسانه,Pro)
admin.site.register(ارزش_های_پیشنهادی,Val)
# admin.site.register(User_type)
# admin.site.register(User)
admin.site.register(منوی_محبوب_رستوران , Me)
admin.site.register(نوع_شبکه_اجتماعی , Pq)
admin.site.register(خبر,Ne)
admin.site.register(نوع_عکس , Pp)
admin.site.register(بنر , Ban)
admin.site.register(سرویس , Ban)
admin.site.register(لوگو , Lo)
# admin.site.register(پانویس)
# admin.site.register(سربرگ)
admin.site.register(نوع_غذا ,Ty)
admin.site.register(منوی_غذا , Fo)
admin.site.register(درباره_ما , Ab)
admin.site.register(تماس_با_ما, Ab)
admin.site.register(شبکه_اجتماعی ,So)
