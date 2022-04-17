from .import views
from django.urls import path
urlpatterns = [
    path('',views.cal),
    #path('/user',views.introduce)
]