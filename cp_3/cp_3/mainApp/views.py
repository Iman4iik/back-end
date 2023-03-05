from rest_framework import generics
from .serializers import *
from .models import *


class ListTodoList(generics.ListCreateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


class DetailTodoList(generics.RetrieveUpdateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


class CreateTodoList(generics.CreateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


class DeleteTodoList(generics.DestroyAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


class ListTodo(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class CreateTodo(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DeleteTodo(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class ListTodos(generics.ListAPIView):
    queryset = Todo.todo_list
    serializer_class = TodosSerializer


class CreateTodos(generics.CreateAPIView):
    queryset = Todo.todo_list
    serializer_class = TodosSerializer
