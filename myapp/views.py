from django.shortcuts import redirect
from django.views import generic
from django.urls import reverse_lazy

from myapp.form import TagForm, TaskForm
from myapp.models import Tag, Task

class TagListView(generic.ListView):
    model = Tag
    template_name = "myapp/tag-list.html"
    context_object_name = "tags"


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    template_name = "myapp/tag_form.html"
    success_url = reverse_lazy("myapp:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "myapp/tag_form.html"
    success_url = reverse_lazy("myapp:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "myapp/tag_confirm_delete.html"
    success_url = reverse_lazy("myapp:tag-list")


class TaskListView(generic.ListView):
    model = Task
    template_name = "myapp/task-list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.order_by("done", "-datetime")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "myapp/task_form.html"
    success_url = reverse_lazy("myapp:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "myapp/task_form.html"
    success_url = reverse_lazy("myapp:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "myapp/task_confirm_delete.html"
    success_url = reverse_lazy("myapp:task-list")


class TaskDoneView(generic.UpdateView):
    def post(self, request, pk=None, *args, **kwargs):
        task = Task.objects.get(pk=pk)
        task.done = not task.done
        task.save()
        return redirect("myapp:task-list")
