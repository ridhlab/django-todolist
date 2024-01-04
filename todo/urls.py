from django.urls import path
from .views import TodoViews, TodoViewsDetail

urlpatterns = [
    path("todo", TodoViews.as_view(), name="todos"),
    path("todo/<str:id>", TodoViewsDetail.as_view(), name="todo-detail"),
]
