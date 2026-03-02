from django.urls import path
from . import views

urlpatterns = [

path('', views.pos_view, name='pos'),

path('create-sale/', views.create_sale, name='create_sale'),

]