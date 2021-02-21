from django.urls import path
from . import views


urlpatterns = [
    path('memes', views.MemePostAll.as_view()), # GET memes, POST memes
    path('memes/<int:id>', views.MemePostSingle.as_view()), # GET memes/<id>, PATCH memes/<id>
    path('tags/<str:tagName>', views.HashTag.as_view()), # GET posts with same tags
    path('count/', views.memeCount.as_view()) # GET number of posts    
]