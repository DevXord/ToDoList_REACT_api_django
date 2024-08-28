from rest_framework import viewsets, status
from .models import Task
from .serializers import TaskSerializer
from rest_framework.decorators import action
from rest_framework.response import Response 
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
import json



class TaskViewSet(viewsets.ViewSet):
    """
    ViewSet do zarządzania zadaniami.
    """

    def list(self, request):
        """
        Pobierz wszystkie zadania: GET /api/tasks/
        """
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Pobierz szczegóły pojedynczego zadania: GET /api/tasks/{id}/
        """
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def get_object(self, pk):
        """
        Pobierz obiekt zadania na podstawie jego ID.
        """
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response({"error": "Task not found."}, status=status.HTTP_404_NOT_FOUND)

   
    @action(detail=True, methods=['delete'], url_path='delete-task')
    def delete_task(self, request, pk=None):
        """
        Usuń zadanie: DELETE /api/tasks/{id}/delete-task/
        """
        task = self.get_object(pk)
        if isinstance(task, Response):  # Obsługa błędu, jeśli zadanie nie istnieje
            return task
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['put'], url_path='update-task')
    def update_task(self, request, pk=None):
        """
        Zaktualizuj zadanie: PUT /api/tasks/{id}/update-task/
        """
        task = self.get_object(pk)
      
        if isinstance(task, Response):  # Obsługa błędu, jeśli zadanie nie istnieje
            return task
    
        serializer = TaskSerializer(task, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CreateTaskViewSet(viewsets.ViewSet):
    """
    ViewSet do dodawania zadań.
    """
    @action(detail=False, methods=['post'], url_path='add-task')
    def add_task(self, request):
        serializer = TaskSerializer(data=request.data)
 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 

