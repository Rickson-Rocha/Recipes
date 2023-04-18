from django.urls import path

from recipes.views import home

# path  - route + views + (optional) name

urlpatterns = [
    path('',home),
]
