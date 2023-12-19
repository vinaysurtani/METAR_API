from django.http import JsonResponse,HttpResponse
from urllib.request import urlopen

from .methods import setinfo
from .models import DataItem
from django.forms.models import model_to_dict
import json
import re
import math
from django.core.cache import cache

# Create your views here.
def ping(request):
    return JsonResponse({'data':'pong'})

def info(request):
    trial={}
    key1=request.GET.get('scode')
    key2=request.GET.get('nocache')
    if key2=="0":
        if cache.get(key1):
            trial=cache.get(key1)
            print(f"get call from cache used {cache.ttl(key1)}")
        else:
            trial = setinfo(key1)
            cache.set(key1, trial, timeout=300)
            print(f"cache is set")
    else:
        trial = setinfo(key1)
        cache.set(key1, trial, timeout=300)
        print(f"cache is set")
    return JsonResponse({'data':trial})