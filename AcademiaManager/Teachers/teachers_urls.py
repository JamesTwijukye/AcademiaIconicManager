
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    path('',views.allTeachers,name='all_teachers'),
    path('add/',views.createTeacher,name='add_teacher'),
    path('<int:teacher_id>/',views.singleTeacher,name='single_teacher'),
    path('<int:pk>/edit',views.editTeacher,name='edit_teacher'),
    path('<int:pk>/delete',views.deleteTeacher,name='delete_teacher'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)