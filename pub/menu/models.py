from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class Categories(models.Model):
    STARTER = "starter"
    FOOD = "food"
    DRINK = "drink"
    SPECIAL = "special"
    OTHER = "other"

    CATEGORY_CHOISES =  [
        (STARTER, "Starter"),
        (FOOD, "Food"),
        (DRINK, "Drink"),
        (SPECIAL, "Special"),
        (OTHER, "Other")
    ]
    
    name = models.CharField(max_length=50, choices=CATEGORY_CHOISES)

    def __str__(self):
        return f"Category: {self.name}"


class Allergens(models.Model):
    GLUTEN_CEREALS = 'gluten_cereals'
    CRUSTACEANS = 'crustaceans'
    EGGS = 'eggs'
    FISH = 'fish'
    PEANUTS = 'peanuts'
    SOY = 'soy'
    DAIRY = 'dairy'
    NUTS = 'nuts'
    CELERY = 'celery'
    MUSTARD = 'mustard'
    SESAME = 'sesame'
    SULPHITES = 'sulphites'
    LUPINS = 'lupins'
    MOLLUSCS = 'molluscs'

    ALLERGEN_CHOICES = [
        (GLUTEN_CEREALS, 'Cereals containing gluten'),
        (CRUSTACEANS, 'Crustaceans'),
        (EGGS, 'Eggs'),
        (FISH, 'Fish'),
        (PEANUTS, 'Peanuts'),
        (SOY, 'Soy'),
        (DAIRY, 'Milk'),
        (NUTS, 'Nuts'),
        (CELERY, 'Celery'),
        (MUSTARD, 'Mustard'),
        (SESAME, 'Sesame'),
        (SULPHITES, 'Sulphur dioxide and sulphites at concentrations higher than 10 mg/kg or mg/l'),
        (LUPINS, 'Lupins'),
        (MOLLUSCS, 'Molluscs'),
    ]

    name = models.CharField(max_length=50, choices=ALLERGEN_CHOICES)

    def __str__(self):
     return f"Allergen: {self.name}"





class MenuItem(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 200, unique = True, blank = False)
    description = models.TextField(blank = True, null = True)
    price = models.IntegerField(null = False)
    category = models.ForeignKey(Categories, on_delete = CASCADE)
    available = models.BooleanField(default = True)
    image_url = models.URLField(blank = True, null = True)
    allergens = models.ManyToManyField(Allergens, related_name='menu_items') 
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'{self.name}'
    

    