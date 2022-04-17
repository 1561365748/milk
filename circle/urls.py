from .import views
from django.urls import path
urlpatterns = [
    path('load',views.load),
    path('friend',views.allsaying),
    path('friend/<int:likeid>',views.add_like)
]