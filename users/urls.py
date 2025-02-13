from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login-page/', views.loginpage, name='loginpage'),
    path('register-page/<user_role>', views.registerpage, name='registerpage'),
    path('select-role/', views.selectrole, name='selectrole'),
    path('dashboard-page/<slug:sg>/', views.dashboardpage, name='dashboardpage'),
    path('user-logout/', views.logoutpage, name='logoutpage'),
    path('edit-profile/', views.editpage, name='editprofile'),
    path('change-pw/', views.changepw, name='changepw'),
]