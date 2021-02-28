from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'menu'
        

class Category(models.Model):
    name = models.CharField(max_length=50)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'categories'
        
class Drink(models.Model):
    name        = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    category    = models.ForeignKey('Category', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'drinks'
        
class Image(models.Model):
    image_url = models.CharField(max_length=2000)
    drink     = models.ForeignKey('Drink', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'images'
        
class Allergy(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'allergies'
    
class Allergy_Drink(models.Model):
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    drink   = models.ForeignKey('Drink', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'allergy_drinks' 