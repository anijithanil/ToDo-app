from .import views
from django.urls import path

urlpatterns = [
    path('', views.index,name='list'),
    path('update_task/<str:pk>/',views.update_task,name='update_task'),
    path('delete/<str:pk>/',views.delete_task,name='delete'),

]