from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100 )
    description = models.TextField(max_length=500)
    completed = models.BooleanField(default=False)
    createed_at = models.DateTimeField(auto_now_add=True, db_index=True)
    completed_at = models.DateTimeField(default=models.SET_NULL,null=models.SET_NULL)
   
    def __str__(self):
        return self.title