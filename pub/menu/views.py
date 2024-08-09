

# Create your views here.


from django.http import JsonResponse
from django.views import View
from .models import MenuItem
import logging


logger = logging.getLogger(__name__)

class MenuItemView(View):
    def get(self, request, *args, **kwargs):
        logger.info("get request")
        
        menu_items = MenuItem.objects.all()

        # Construct a list of dictionaries with related names
        data = [
            {
                'id': item.id,
                'name': item.name,
                'description': item.description,
                'price': item.price,
                'category': item.category.name, 
                'available': item.available,
                'image_url': item.image_url,
                'allergens': [allergen.name for allergen in item.allergens.all()],  
                'created_at': item.created_at.isoformat(),
                'updated_at': item.updated_at.isoformat(),
            }
            for item in menu_items
        ]

       
        return JsonResponse(data, safe=False)