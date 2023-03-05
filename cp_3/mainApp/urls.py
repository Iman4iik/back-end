from django.urls import path
from .views import *
urlpatterns = [
    path('<int:pk>/', DetailTodoList.as_view()),
    path('', ListTodoList.as_view()),
    path('create', CreateTodoList.as_view()),
    path('delete/<int:pk>', DeleteTodoList.as_view()),

    path('todos/<int:pk>/', DetailTodo.as_view()),
    path('todos/', ListTodo.as_view()),
    path('todos/create', CreateTodo.as_view()),
    path('todos/delete/<int:pk>', DeleteTodo.as_view()),

    path('<int:pk>/todos', ListTodo.as_view()),
    path('<int:pk>/todos/create', CreateTodos.as_view()),
]