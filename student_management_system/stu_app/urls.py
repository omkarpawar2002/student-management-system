from django.urls import path
from .views import ( CreateStudentView,ShowStudentView,UpdateStudentView,DeleteStudentView )

urlpatterns = [
    path('create_stu/',CreateStudentView.as_view(),name='create_stu'),
    path('show_stu/',ShowStudentView.as_view(),name='show_stu'),
    path('update_stu/<int:pk>/',UpdateStudentView.as_view(),name='update_stu'),
    path('delete_stu/<int:pk>/',DeleteStudentView.as_view(),name='delete_stu')
]