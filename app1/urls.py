from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add/',views.add_form,name='add_form'),
    path('delete/<id>',views.delete,name='delete'),

]
