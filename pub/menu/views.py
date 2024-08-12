

# Create your views here.


from django.http import JsonResponse, HttpResponse
from django.views import View
from .models import MenuItem
from django.db import DatabaseError
import logging


logger = logging.getLogger(__name__)

class MenuItemView(View):
    def get(self, request, *args, **kwargs):
        logger.info("Recived a get request for MenuItem")

        try:


        
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
        

        
        except DatabaseError as dbe : 
            logger.error(f"DatabaseError occurred : {dbe}")
            return HttpResponse(status=500)
        
        except Exception as e :
            logger.error(f"Unexpected error : {e}")
            return HttpResponse(status=500)