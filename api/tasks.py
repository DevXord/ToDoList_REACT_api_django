from django_q.tasks import schedule, Schedule
from datetime import timedelta
from .models import Task
import os

def reset_server(): 
    Task.objects.all().delete()
    print("Restart serwera...")
    os._exit(3)  # Kod 3 powoduje restart w autoreloaderze
    
# Harmonogram uruchamiania co minutę
schedule(
    'reset_server',
    schedule_type=Schedule.MINUTES,
    minutes=1
    
)