
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime
from django.utils import timezone
# from .user_typemodel.py import User_type

class رسانه(models.Model):
    شناسه = models.AutoField(primary_key=True)
    فایل =  models.FileField(upload_to='Media/' , help_text = "عکس را در اینجا بارگذاری کنید")
    توضیح = models.CharField(max_length = 500)
    عنوان = models.CharField(max_length = 500)
    جایگزین = models.CharField(max_length = 500  , help_text = "یک جایگزین مناسب برای عکس وارد کنید تا در صورت نیاز بجای عکس نمایش داده شود.")
    حذف = models.IntegerField(default = 0 , help_text= "در این قسمت هر عددی که جایگزین 0 شود به معنی حذف شدن این نمونه از سایت است.")

    class Meta:
        verbose_name_plural = "رسانه"

    def __str__(self):
        return str(self.شناسه)


class ارزش_های_پیشنهادی(models.Model):

    شناسه = models.AutoField(primary_key=True)
    ارزش_پیشنهادی = models.CharField(max_length=500)
    شناسه_عکس = models.ForeignKey(رسانه,on_delete=models.CASCADE , help_text = "شناسه رسانه مورد نظر را انتخاب کرده یا رسانه ای جدید ایجاد کنید.")
    حذف = models.IntegerField(default = 0 , help_text= "در این قسمت هر عددی که جایگزین 0 شود به معنی حذف شدن این نمونه از سایت است.")

    class Meta:
        verbose_name_plural = "ارزش_های_پیشنهادی"

    def __str__(self):
            return self.ارزش_پیشنهادی

class منوی_محبوب_رستوران(models.Model):

    شناسه = models.AutoField(primary_key=True)
    عنوان_غذا = models.CharField(max_length=500)
    توضیح = models.CharField(max_length=500)
    شناسه_عکس = models.ForeignKey(رسانه,on_delete=models.CASCADE , help_text = "شناسه رسانه مورد نظر را انتخاب کرده یا رسانه ای جدید ایجاد کنید.")
    جایگزین = models.CharField(max_length = 500  , help_text ="یک جایگزین مناسب برای عکس وارد کنید تا در صورت نیاز بجای عکس نمایش داده شود.")
    حذف = models.IntegerField(default = 0 , help_text= "در این قسمت هر عددی که جایگزین 0 شود به معنی حذف شدن این نمونه از سایت است.")

    class Meta:
        verbose_name_plural = "منوی_محبوب_رستوران"

    def __str__(self):
            return self.عنوان_غذا

social_networks=(
('Instagram','Instagram'),
('Telegram','Telegram')
)

class نوع_شبکه_اجتماعی(models.Model):
    شناسه = models.AutoField(primary_key=True)
    متن = models.CharField(max_length = 500 , choices = social_networks)
    حذف = models.IntegerField(default = 0 , help_text= "در این قسمت هر عددی که جایگزین 0 شود به معنی حذف شدن این نمونه از سایت است.")

    class Meta:
        verbose_name_plural = "نوع_شبکه_اجتماعی"

    def __str__(self):
        return self.متن


class خبر(models.Model):

    شناسه = models.AutoField(primary_key=True)
    عنوان_خبر=models.CharField(max_length=500)
    شرح_خبر = RichTextUploadingField()
    تاریخ = models.DateField(default=timezone.now)
    شناسه_عکس = models.ForeignKey(رسانه,on_delete=models.CASCADE, null=True, blank =True ,
    default=None ,max_length = 500 , related_name='nmedia' , help_text = "شناسه رسانه مورد نظر را انتخاب کرده یا رسانه ای جدید ایجاد کنید.")
    شناسه_عکس_مارکتینگ= models.ForeignKey(رسانه,on_delete=models.CASCADE, null=True, blank =True ,
    default=None ,max_length = 500 , related_name='nmarketing' , help_text = "شناسه رسانه مورد نظر را انتخاب کرده یا رسانه ای جدید ایجاد کنید.")
    متن_مارکتینگ=models.CharField(max_length=500)
    پارامتر_کمکی = models.CharField(max_length=500 , null=True, blank =True)
    جایگزین = models.CharField(max_length = 500  , help_text ="یک جایگزین مناسب برای عکس وارد کنید تا در صورت نیاز بجای عکس نمایش داده شود.")
    حذف = models.IntegerField(default = 0 , help_text= "در این قسمت هر عددی که جایگزین 0 شود به معنی حذف شدن این نمونه از سایت است.")

    class Meta:
        verbose_name_plural = "خبرها"


    def __str__(self):
        return str(self.شناسه)

banner_type=(
    ('صفحه اصلی','صفحه اصلی'),
    ('صفحه اخبار','صفحه اخبار'),
    ('صفحه تماس با ما','صفحه تماس با ما'),
    ('صفحه درباره ما','صفحه درباره ما'),
    ('صفحه منوی غذا' , 'صفحه منوی غذا'),
)
class نوع_عکس(models.Model):
    شناسه = models.AutoField(primary_key=True)
    نوع = models.CharField(max_length = 500, choices = banner_type , unique = True)
    حذف = models.IntegerField(default = 0 , help_text= "در این قسمت هر عددی که جایگزین 0 شود به معنی حذف شدن این نمونه از سایت است.")

    class Meta:
        verbose_name_plural= 'نوع_عکس_ها'

    def __str__(self):
        return self.نوع


class بنر(models.Model):

    شناسه = models.AutoField(primary_key=True)
    عنوان = models.CharField(max_length = 500)
    زیرنویس = models.CharField(max_length = 500)
    شناسه_بنر  = models.ForeignKey(رسانه,on_delete=models.CASCADE , help_text = "شناسه رسانه مورد نظر را انتخاب کرده یا رسانه ای جدید ایجاد کنید.")
    نوع = models.ForeignKey(نوع_عکس,on_delete=models.CASCADE)
    جایگزین = models.CharField(max_length = 500  , help_text ="یک جایگزین مناسب برای عکس وارد کنید تا در صورت نیاز بجای عکس نمایش داده شود.")

    حذف = models.IntegerField(default = 0 , help_text= "در این قسمت هر عددی که جایگزین 0 شود به معنی حذف شدن این نمونه از سایت است.")

    class Meta:
        verbose_name_plural= 'بنر_ها'

    def __str__(self):
        return str(self.شناسه)


class سرویس(models.Model):

    شناسه = models.AutoField(primary_key=True)
    عنوان = models.CharField(max_length = 500)
    زیرنویس = models.CharField(max_length = 500)
    شناسه_عکس = models.ForeignKey(رسانه,on_delete=models.CASCADE, null=True, blank =True ,
    default=None ,max_length = 500 , related_name='cmedia' , help_text = "شناسه رسانه مورد نظر را انتخاب کرده یا رسانه ای جدید ایجاد کنید.")

    پارامتر_کمکی = models.CharField(max_length = 500 , null=True, blank =True)
    جایگزین = models.CharField(max_length = 500  , help_text ="یک جایگزین مناسب برای عکس وارد کنید تا در صورت نیاز بجای عکس نمایش داده شود.")
    حذف = models.IntegerField(default = 0 , help_text= "در این قسمت هر عددی که جایگزین 0 شود به معنی حذف شدن این نمونه از سایت است.")

    class Meta:
        verbose_name_plural = "سرویس_ها"
    def __str__(self):
        return str(self.شناسه)

class لوگو(models.Model):

    شناسه = models.AutoField(primary_key=True)
    متن = models.CharField(max_length = 500)
    شناسه_لوگو = models.ForeignKey(رسانه,on_delete=models.CASCADE , help_text = "شناسه رسانه مورد نظر را انتخاب کرده یا رسانه ای جدید ایجاد کنید.")
    جایگزین = models.CharField(max_length = 500  , help_text ="یک جایگزین مناسب برای عکس وارد کنید تا در صورت نیاز بجای عکس نمایش داده شود.")
    حذف = models.IntegerField(default = 0 , help_text= "در این قسمت هر عددی که جایگزین 0 شود به معنی حذف شدن این نمونه از سایت است.")

    class Meta:
        verbose_name_plural = "لوگو"
    def __str__(self):
        return str(self.شناسه)


class پانویس(models.Model):
    شناسه = models.AutoField(primary_key=True)
    متن = models.CharField(max_length = 500)
    لینک = models.CharField(max_length=500)
    حذف = models.IntegerField(default = 0 , help_text= "در این قسمت هر عددی که جایگزین 0 شود به معنی حذف شدن این نمونه از سایت است.")

    class Meta:
        verbose_name_plural = "پانویس"

    def __str__(self):
        return str(self.شناسه)


class سربرگ(models.Model):
    شناسه = models.AutoField(primary_key=True)
    متن = models.CharField(max_length = 500)
    لینک = models.CharField(max_length=500)
    حذف = models.IntegerField(default = 0 , help_text= "در این قسمت هر عددی که جایگزین 0 شود به معنی حذف شدن این نمونه از سایت است.")

    class Meta:
        verbose_name_plural = "سربرگ"

    def __str__(self):
        return str(self.شناسه)

# class Costumer(models.Model):
#
#     # id = models.AutoField(primary_key=True)
#     text = models.CharField(max_length = 500)
#     logo_id = models.ForeignKey(رسانه,on_delete=models.CASCADE , help_text = "شناسه رسانه مورد نظر را انتخاب کرده یا رسانه ای جدید ایجاد کنید.")
#     deleted = models.IntegerField(default = 0)

class منوی_غذا(models.Model):

    شناسه = models.AutoField(primary_key=True)
    عنوان = models.CharField(max_length=500)
    محتویات = models.CharField(max_length=500 , help_text = "محتویات غذا را به صورت مختصر بنویسید.")
    متن = RichTextUploadingField()
    شناسه_عکس = models.ForeignKey(رسانه,on_delete=models.CASCADE , help_text = "شناسه رسانه مورد نظر را انتخاب کرده یا رسانه ای جدید ایجاد کنید.")
    جایگزین = models.CharField(max_length = 500  , help_text ="یک جایگزین مناسب برای عکس وارد کنید تا در صورت نیاز بجای عکس نمایش داده شود.")
    حذف = models.IntegerField(default = 0 , help_text= "در این قسمت هر عددی که جایگزین 0 شود به معنی حذف شدن این نمونه از سایت است.")

    class Meta:
        verbose_name_plural = "منوی_غذا"

    def __str__(self):
        return str(self.شناسه)


class درباره_ما(models.Model):
    شناسه = models.AutoField(primary_key=True)
    عکس۱ = models.ForeignKey(رسانه,on_delete=models.CASCADE , related_name='ax1', help_text = "شناسه رسانه مورد نظر را انتخاب کرده یا رسانه ای جدید ایجاد کنید.")
    عکس۲ = models.ForeignKey(رسانه,on_delete=models.CASCADE , related_name='ax2', help_text = "شناسه رسانه مورد نظر را انتخاب کرده یا رسانه ای جدید ایجاد کنید.")
    متن = models.TextField()
    جایگزین = models.CharField(max_length = 500  , help_text ="یک جایگزین مناسب برای عکس وارد کنید تا در صورت نیاز بجای عکس نمایش داده شود.")
    حذف = models.IntegerField(default = 0 , help_text= "در این قسمت هر عددی که جایگزین 0 شود به معنی حذف شدن این نمونه از سایت است.")

    class Meta:
        verbose_name_plural = "درباره_ما"

    def __str__(self):
        return str(self.شناسه)


class تماس_با_ما(models.Model):
    شناسه = models.AutoField(primary_key=True)
    آدرس = models.CharField(max_length=500)
    ایمیل = models.EmailField(max_length=500)
    تلفن = models.CharField(max_length=500 , help_text='شماره های تماس را با الگوی روبرو وارد کنید: ۱۲۳۴۵۶ − ۱۲۳۴۵۶.')
    طول_جغرافیایی = models.FloatField(help_text='طول جغرافیایی رستوران را با دقت دو رقم اعشار وارد کنید.')
    عرض_جغرافیایی = models.FloatField(help_text='عرض جغرافیایی ریتوران را با دقت دو رقم اعشار وارد کنید.')
    حذف = models.IntegerField(default = 0 , help_text= "در این قسمت هر عددی که جایگزین 0 شود به معنی حذف شدن این نمونه از سایت است.")

    class Meta:
        verbose_name_plural = "تماس_با_ما"

    def __str__(self):
        return str(self.شناسه)

class شبکه_اجتماعی(models.Model):
    شناسه = models.AutoField(primary_key=True)
    نام_کاربری = models.CharField(max_length = 500)
    نوع_شبکه_اجتماعی = models.ForeignKey(نوع_شبکه_اجتماعی,on_delete=models.CASCADE)
    حذف = models.IntegerField(default = 0 , help_text= "در این قسمت هر عددی که جایگزین 0 شود به معنی حذف شدن این نمونه از سایت است.")

    class Meta:
        verbose_name_plural = "شبکه_اجتماعی"

    def __str__(self):
        return self.نام_کاربری

# p = نوع_شبکه_اجتماعی.objects.create(متن = "Instagram")
# q = نوع_شبکه_اجتماعی.objects.create(متن = "Telegram")
# r = نوع_عکس.objects.create(نوع = "صفحه اصلی")
# s = نوع_عکس.objects.create(نوع = "صفحه اخبار")
# t = نوع_عکس.objects.create(نوع = "صفحه تماس با ما")
# u = نوع_عکس.objects.create(نوع = " صفحه درباره ما")
# v = نوع_عکس.objects.create(نوع = "صفحه منوی غذا")
