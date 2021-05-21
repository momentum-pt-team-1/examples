from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=280)
    created_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(blank=True, null=True)
    done = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos")
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name="todos", blank=True, null=True)

    def __str__(self):
        return self.text


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name








