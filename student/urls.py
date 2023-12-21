from django.urls import path
from . import views

app_name = 'student'
urlpatterns = [
    path('', views.StudentList.as_view(), name='student_list'),
    path('new/', views.StudentCreate.as_view(), name='student_new'),
    path('<int:pk>/edit/', views.StudentUpdate.as_view(), name='student_edit'),
    path('<int:pk>/delete/', views.StudentDelete.as_view(), name='student_delete'),
]
