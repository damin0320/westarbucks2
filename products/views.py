import json


from django.views import View
from django.http  import JsonResponse


from .models import *

class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        result = []
        
        for category in categories:
            my_dict = {
                'name' : category.name,
                'menu' : category.menu.name
            }
            result.append(my_dict)
        
        return JsonResponse({'result' : result}, status=200)
    
    def post(self, request):
        data     = json.loads(request.body)
        menu     = Menu.objects.get(name=data['menu'])
        category = Category.objects.create(
            name = data["name"],
            menu = menu
        )
        return JsonResponse({"MESSAGE" : "SUCCESS"}, status = 201)
    

class DrinkView(View):
    def get(self, request):
        drinks = Drink.objects.all()
        result = []
        
        for drink in drinks:
            my_dict = {
                'name'        : drink.name,
                'description' : drink.description,
                'category'    : drink.category.name
            }
            result.append(my_dict)
        return JsonResponse({'result' : result}, status=200) 
    
    def post(self, request):
        data     = json.loads(request.body)
        category = Category.objects.get(name=data['category'])
        drink    = Drink.objects.create(
        
            name        = data['name'],
            description = data["description"],
            category    = category
        )
        
        return JsonResponse({"MESSAGE" : "SUCCESS"}, status = 201)
    
class ImageView(View):
    def get(self, request):
        images = Image.objects.all()
        result = []
        
        for image in images:
            my_dict = {
                'image_url' : image.image_url,
                'drink'     : image.drink.name
            }
            result.append(my_dict)
        return JsonResponse({'result' : result}, status=200) 
    
    def post(self, request):
        data      = json.loads(request.body)
        drink     = Drink.objects.get(name=data['drink'])
        image_url = Image.objects.create(
        
            image_url = data['image_url'],
            drink     = drink
        )
        
        return JsonResponse({"MESSAGE" : "SUCCESS"}, status = 201)

class AllergyDrink(View):
    def get(self, request):
        allergy_drinks = Allergy_Drink.objects.all()
        result = []
        
        for allergy_drink in allergy_drinks:
            my_dict = {
                'allergy' : allergy_drink.allergy.name,
                'drink'   : allergy_drink.drink.name
            }
            result.append(my_dict)
        return JsonResponse({'result' : result}, status=200)
    
    def post(self, request):
        data    = json.loads(request.body)
        drink   = Drink.objects.get(name=data['drink'])    
        allergy = Allergy.objects.get(name=data['allergy'])
        
        allergy_drink = Allergy_Drink.objects.create(
            allergy = allergy,
            drink   = drink)
        return JsonResponse({"MESSAGE" : "SUCCESS"}, status = 201)