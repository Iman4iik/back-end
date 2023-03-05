from rest_framework import serializers
from .models import *


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ('id', 'title', 'description', 'completed')


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed', 'todo_list')


class TodosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('todo_list',)