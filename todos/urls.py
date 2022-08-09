from django.urls import path
from todos.views import TodosAPIView, TodoDetailAPIView

urlpatterns = [
    path("", TodosAPIView.as_view(), name="todos"),
    path("<int:pk>/", TodoDetailAPIView.as_view(), name="todo-detail"),
]
