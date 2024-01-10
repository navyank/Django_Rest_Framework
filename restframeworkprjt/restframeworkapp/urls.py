from django.urls import path
from .import views


urlpatterns = [
    path('',views.apiOverView, name="api-overview"),
    path('task-list/',views.tasklist, name="task-list"),
    path('task-details/<str:pk>/',views.taskdetails, name="task-details"),
    path('task-create/',views.taskcreate, name="task-create"),
    path('task-update/<str:pk>/',views.taskupdate, name="task-update"),
     path('task-delete/<str:pk>/',views.taskdelete, name="task-delete"),
    
     
]
