from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
import requests
from .models import raw_data
from . import variables
import re
# Create your views here.

@csrf_exempt
def data_entry(request):
    url = variables.phone_server
    response = requests.get(url)
    
    data = response.json()
    for i in range(len(data)):
        sender = data[i]['address']
        message = data[i]['body']
        message_id = int(data[i]['id'])
        time = data[i]['received']
        data_entry = raw_data(sender = sender, message = message, message_id = message_id, time = time )
        data_entry.save()

def getting_db(request):
    sms_obj = raw_data.objects.all()
    li = [] #for testing purpose only
    ids = sms_obj.values_list('message_id', flat=True) #getting list of messages id
    for id in ids: 
        sender_id = raw_data.objects.filter(message_id=id).values_list('sender', flat=True).first() #getting first bacause duplicate in db
        pattern = r'HDFC|BOI|KOTAK' #getting messages only from banks
        match = re.search(pattern, sender_id)
        if match:
            bank_data = sms_obj.filter(message_id=id).values().first()
            li.append(bank_data)
    data = li
    return render(request, 'mongoose/index.html',{
    'data': data
    })
        