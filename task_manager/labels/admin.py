from django.contrib import admin
from task_manager.labels.models import Label


class LabelModelAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Label, LabelModelAdmin)
