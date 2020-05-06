from django.urls import path
from details_app import views

urlpatterns = [
    path('',views.check,name='index'),

]
