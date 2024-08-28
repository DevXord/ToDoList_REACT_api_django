from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed','createed_at' , 'completed_at']
        read_only_fields = ['created_at']  # Dodaj tylko te pola, które rzeczywiście powinny być tylko do odczytu

 