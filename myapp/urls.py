from django.urls import path

from myapp.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TaskDoneView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task/add/", TaskCreateView.as_view(), name="task-add"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(),
         name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(),
         name="task-delete"),
    path("task/<int:pk>/done/", TaskDoneView.as_view(), name="task-done"),
    path("tag/", TagListView.as_view(), name="tag-list"),
    path("tag/add/", TagCreateView.as_view(), name="tag-add"),
    path("tag/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "myapp"
