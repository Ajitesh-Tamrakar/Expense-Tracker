from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.

@csrf_exempt
def data_entry(request):
    if request.method == 'POST':
        try:
            body_unicode = request.body.decode('utf-8')
            data_list = json.loads(body_unicode)
            for data in data_list:                
                print(data['message'])
            return JsonResponse({'message': 'data recived'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'invalid json'}, status= 400)
    return JsonResponse({'error': 'only POST method is allowed'}, status=405)
    
