from django.urls import path
from .views import *

urlpatterns = [
    path('/category', CategoryView.as_view()),
    path('/drink', DrinkView.as_view()),
    path('/image', ImageView.as_view()),
    path('/allergydrink', AllergyDrink.as_view()),    
]