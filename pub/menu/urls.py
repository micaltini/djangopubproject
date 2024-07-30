from django.urls import path
from .views import MenuItemView

urlpatterns = [

path('', MenuItemView.as_view(), name='menu_items')

]