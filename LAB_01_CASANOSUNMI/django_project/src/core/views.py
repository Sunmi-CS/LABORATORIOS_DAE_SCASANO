from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Item
import json

def item_list(request):
    items = Item.objects.all()
    return render(request, 'core/item_list.html', {'items': items})

# API: listar items
def api_items(request):
    items = list(Item.objects.values())
    return JsonResponse(items, safe=False)

# API: crear item
@csrf_exempt
def api_add_item(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item = Item.objects.create(
            name=data.get('name'),
            description=data.get('description', '')
        )
        return JsonResponse({'id': item.id, 'name': item.name, 'description': item.description})
    return JsonResponse({'error': 'Invalid request'}, status=400)
