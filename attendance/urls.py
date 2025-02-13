from django.urls import path
from . import views

urlpatterns = [
    path('my-attendance/<slug:sg>/', views.myattendance, name='attendancehistory'),
    path('assigned-teachers/', views.teachersassgined, name='teachersassgined'),
    path('all-student/', views.allstudent, name='allstudent'),
    path('student-details/<slug:sg>/', views.studentdetails, name='studentdetails'),
    path('selectgrade-attendance/', views.selectgradeattend, name='selectgradeattend'),
    path('take-attendance/<int:gradelevel>/', views.takeattendance, name='takeattendance'),
    path('selectattendance-history/', views.selectattendancehistory, name='selectattendancehistory'),
    path('student-attendance-history/<int:gradelevel>/', views.studentsattendancehistory, name='studentsattendancehistory'),
]