from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  TaskViewSet, CreateTaskViewSet, ResetTasksView

router = DefaultRouter()
 
router.register(r'tasks', TaskViewSet, basename='tasks') 
router.register(r'', CreateTaskViewSet, basename='') 
 
urlpatterns = [
    path('', include(router.urls)),
    path('reset-tasks/', ResetTasksView.as_view(), name='reset-tasks'),
   
  
] 