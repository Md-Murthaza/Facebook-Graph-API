from django.shortcuts import render,HttpResponse
import requests
from django.http import JsonResponse 
import requests
from django.views.decorators.csrf import csrf_exempt


# Using User Access Token to see the page id and details of it
ACCESS_TOKEN = 'EAAZAOZC00MBqABOw22ZB4YbZAdzioUoC56Py3ZCBlZCgvp9OGntKPNoAkmmrRWlD3gAJHyPJPUYv4XTJmT0vria8ZAZC4IKUxhPBnIiMHjDxS2OJYt0fXN4L4i9esi0ZCtvEZAmo1jlefMZBcyWsZBDAY8VbEILZB0ZA8xPsfuSZADciGz9HzdBXwKKZCTxb7BAxM6ZB6eQckM5iMZBc2eVOhi1m0KOZBK1SAO3egZDZD'

def facebook_profile_view(request):
    url = 'https://graph.facebook.com/v16.0/me/accounts'
    params = {
        'fields': 'id,name',
        'access_token': ACCESS_TOKEN
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200: 
        return JsonResponse(response.json())
    else:
        return JsonResponse({'error': 'Failed to fetch data from Facebook API'})


#Post to  Facebook

PAGE_ACCESS_TOKEN = 'EAAZAOZC00MBqABOz6IKVicoiHZAzsvGDOCTbzJHii2mn6HGXLpfZCcrynhm9ZBaEF1RiSDWc7mpJGvk0gQ4WE2PJrEZCJ6692V8HNSuAZACpAGRAzJRKkrhHxuZCAQAIiPBLmgWZCyftxbV1C16AVvCck3UnSpT2G7leNUogoUp9gUpXNuDpWXnimOMtH2ZAoqZBQiL'
PAGE_ID = '530451523485260'

@csrf_exempt
def post_to_facebook(request):
    if request.method == 'POST':
        image_file = request.FILES.get('image')
        caption = request.POST.get('caption', '')
        
        url = f'https://graph.facebook.com/v16.0/{PAGE_ID}/photos'
        files = {'file': image_file}
        data = {
            'caption': caption,
            'access_token': PAGE_ACCESS_TOKEN
        }
        
        response = requests.post(url, files=files, data=data)
        
        if response.status_code == 200:
            return JsonResponse({
                'message': 'Image posted successfully!',
                'post_id': response.json().get('id'),
                'details': response.json()
            })
        else:
            return JsonResponse({'error': 'Failed to post to Facebook'}, status=response.status_code)
    return render(request , 'post_facebook.html')





#insights for my fb page

def fetch_page_insights(request):
    url = f'https://graph.facebook.com/v16.0/{PAGE_ID}/insights'
    params = {
        'metric': 'page_impressions',
        'access_token': PAGE_ACCESS_TOKEN
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return JsonResponse(response.json())
    else:
        return JsonResponse({'error': 'Failed to fetch page insights from Facebook API'})
