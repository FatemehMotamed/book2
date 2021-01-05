from django.urls import path

from home.views import *

urlpatterns = [
    path('index/', index),
    path('author/', create_author,name="create_author"),
    path('publisher/', create_publisher,name="create_publisher"),
    path('book/', create_book,name="create_book"),

]
