from django.urls import path
from .import views
urlpatterns = [
    path('', views.list),
    # on rajoute un parametre nomer 
    path('posts/<int:id>/', views.show),
]
