from django.urls import path

from .views import *

urlpatterns = [

    path('', get_tasks),

    path('create/', create_task),

    path('delete/<int:pk>/', delete_task),

]