from django.urls import path
from task_manager.tasks import views

app_name = 'tasks'

urlpatterns = [
    path('', views.TaskListView.as_view(), name='list'),
    path('create/', views.TaskCreateView.as_view(), name='create'),
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(), name='delete'),
    path('<int:pk>', views.TaskDetailsView.as_view(), name='details'),
    path('<int:pk>/update/', views.TaskUpdateView.as_view(), name='update'),
]
