from django.shortcuts import render
from django.http import HttpResponse,JsonResponse, Http404
from .models import tweet
import random

# Create your views here.
def home_view (request, *args, **kwargs):
    # return HttpResponse("<h1> Hello Twitter</h1>")
    return render (request, "pages/home.html", context={}, status = 200)

def tweets_list_view(request, *args, **kwargs):
    qs = tweet.objects.all()
    tweets_list = [{"id": x.id,"content": x.content, "likes" : random.randint(0,123)} for x in qs]
    data = {
        "isUser": False,
        "response": tweets_list
    }
    return JsonResponse(data)

def tweet_detail_view (request, tweet_id, *args, **kwargs):
    data = {
        "id" : tweet_id,   
    }
    status = 200 
    try:
        obj = tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
        

    except:
        data['message'] = "Not found"
        status = 404

    print("Data:", data)     

    return JsonResponse(data, status = status) 
    # return HttpResponse(f"<h1>Hello {tweet_id} - {obj.content}</h1>") 