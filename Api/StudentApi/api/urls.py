from django.urls import path
from api import views

urlpatterns = [
    path("students/", views.StudentListView.as_view()),
    path("students/<int:pk>", views.StudentDetailsView.as_view()),
    path("students_create/", views.StudentCreate.as_view()),
    path("student_update/<int:pk>", views.StudentUpdate.as_view()),
    path("delete_students/<int:pk>", views.StudentDelete.as_view()),

]
