from django.conf.urls import url,include
from django.contrib import admin
from mesineapp import views
from mesineapp.controllers import homepage,collection,news,footer,menu,logo,sendmail,contact_us,media,aboutus,food,header,social_network
from django.conf.urls.static import static
from django.conf import settings






urlpatterns = [
    url(r'^back_end/admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # url(r'^back_end/value_proposition/',site.value_proposition,name='value_proposition'),
    # url(r'^value_proposition/',include('value_proposition.urls')),
    url(r'^back_end/homepage-banner/',homepage.banner,name='banner'),
    url(r'^back_end/services/',homepage.services,name='services'),
    url(r'^back_end/favorite/',homepage.favorite,name='favorite'),
    url(r'^back_end/value_proposition/',homepage.value_proposition,name='value_proposition'),
    # url(r'^back_end/assist-company/',homepage.assist_company,name='assist_company'),
    # url(r'^back_end/value-proposition/',homepage.value_proposition,name='value_proposition'),
    # url(r'^back_end/other-program/',homepage.other_program,name='other_program'),
    url(r'^back_end/collection-card/',collection.collection_card,name='collection_card'),
    url(r'^back_end/collection-slider/',collection.collection_slider,name='collection_slider'),
    url(r'^back_end/collection-content/',collection.collection_content,name='collection_content'),
    url(r'^back_end/collection-search/',collection.collection_search,name='collection_search'),
    url(r'^back_end/menu-banner',menu.banner,name='banner'),
    url(r'^back_end/footer',footer.footer,name='footer'),
    url(r'^back_end/header',header.header,name='header'),
    url(r'^back_end/logo',logo.logo,name='logo'),
    url(r'^back_end/news-card/',news.news_card,name='news_card'),
    url(r'^back_end/news-content',news.news_content,name='news_content'),
    url(r'^back_end/news-search',news.news_search,name='news_search'),
    url(r'^back_end/news-banner',news.banner,name='banner'),
    url(r'^back_end/send-mail',sendmail.email,name='email'),
    url(r'^back_end/contact-us',contact_us.contact_us,name='contact_us'),
    url(r'^back_end/contactus-banner',contact_us.banner,name='banner'),
    url(r'^back_end/media-analayzer',media.media_analyzer,name='media_analyzer'),
    url(r'^back_end/about-us',aboutus.about_us,name='about_us'),
    url(r'^back_end/aboutus-banner',aboutus.banner,name='banner'),
    url(r'^back_end/social-network',social_network.social_network,name='social_network'),
    # url(r'^back_end/parent',parent.parent,name='parent'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
