from django.urls import path
from . import views


urlpatterns = [
    path('', views.AllStudents, name='all_students'),
    path('add/', views.createStudent, name='add_student'),
    path('<int:student_id>/', views.SingleStudents, name='single_student'),
    path('<int:pk>/edit/', views.editStudent, name='edit_student'),
    path('<int:pk>/delete/', views.deleteStudent, name='delete_student')
]
