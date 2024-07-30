

# Create your views here.

from django.http import JsonResponse
from django.core.serializers import serialize
from django.views import View
from .models import MenuItem

class MenuItemView(View):
    def get(self, request, *args, **kwargs):
        
        menu_items = MenuItem.objects.all()

        
        data = serialize('json', menu_items, use_natural_primary_keys=True)

        
        return JsonResponse(data, safe=False)