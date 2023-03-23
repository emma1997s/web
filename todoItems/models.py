from django.db import models
from django.contrib.auth.models import User
    
class Todo(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering = ['-updated', '-created']
    
    def __str__(self) -> str:
        return self.item
    