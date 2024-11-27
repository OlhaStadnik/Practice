from django.contrib import admin

from myapp.models import Task, Tag

admin.site.register(Task)
admin.site.register(Tag)
