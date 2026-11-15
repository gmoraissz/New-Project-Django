from django.urls import path
from recipes.views import *


urlpatterns = [
    path('', home, name='home'), # Home page
    path('contato/', contato, name='contato'), # Contact page
    path('sobre/', sobre, name='sobre') # About page
]
