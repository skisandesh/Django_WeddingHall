from django.contrib import admin
from django.urls import path, include
from . import  views
from django.views.generic import TemplateView


urlpatterns = [

    # path('', TemplateView.as_view(template_name='sites/home.html') ,name='home'),
    path('',views.home,name='home'),
    path('search/',TemplateView.as_view(template_name='sites/search.html'),name='search'),
    path('hall_list/',views.hall_data, name = 'data'),
    path ('contact/',views.contact,name='contact'),
    path('book_hall/<hall_name>/',views.book_hall, name='bookhall' ),
    path('detail/<hall_name>/',views.detailview.as_view(),name='hall_detail'),
    path('my_list/',views.my_list,name='my_list'),

]