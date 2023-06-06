from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
  

    #User
    path('index/', views.index, name='index'),
    path('<int:id>', views.view_employee, name='view_employee'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    

]