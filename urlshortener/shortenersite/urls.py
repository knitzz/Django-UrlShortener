from django.conf.urls import url,include
from .views import index ,about,contact, redirect_original ,shorten_url 

urlpatterns = [
	url(r'^$', index , name='home'),
    # for our home/index page
 
    url(r'^(?P<short_id>[\w]{6})$', redirect_original , name='redirectoriginal'),
    # when short URL is requested it redirects to original URL
 	url(r'^about/$', about, name='about'),
 	url(r'^contact/$', contact, name='contact'),
    url(r'^makeshort/$', shorten_url, name='shortenurl'),
 
]
