from django.contrib import admin
from task_manager.statuses.models import Status


class StatusModelAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Status, StatusModelAdmin)
