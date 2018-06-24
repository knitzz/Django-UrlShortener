from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseRedirect,Http404
from django.core.validators import URLValidator
from .models import Urls

# Create your views here.

def index(request):
	return render(request,"index.html",context={})

def about(request):
	return render(request,"about.html",context={})

def contact(request):
	return render(request,"contact.html",context={})




def redirect_original(request,short_id):

	
	if(Urls.objects.filter(short_id=short_id).exists()):
		obj=Urls.objects.filter(short_id=short_id)[0]
		obj.count+=1
		obj.save()
		return HttpResponseRedirect(obj.httpurl)

	else:
		raise Http404("Given Link Does Not Exist :(") 


def shorten_url(request):
	SITE_URL = "http://localhost:8000/"
	context={}
	url=request.POST.get("url")
	ob=URLValidator()
	try:
		ob(url)
		if(Urls.objects.filter(httpurl=url).exists()):
			# context['exists']='exist'
			short_id=Urls.objects.filter(httpurl=url)[0].short_id
			return render(request,"index.html",context={'short_id':SITE_URL+short_id,'exists':True})
		else:
			short_url=Urls.makeshort()
			newob=Urls.objects.create(httpurl=url,short_id=short_url)
			return render(request,"index.html",context={'short_id':SITE_URL+short_url})
	except:
		return render(request,"index.html",context={'notvalid':'notvalid'})


