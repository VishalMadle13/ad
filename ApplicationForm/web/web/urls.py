"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.HomeView.as_view(), name='home'),
#     path('courses/', views.CourseListView.as_view(), name='course_list'),
#     path('courses/create/', views.CourseCreateView.as_view(), name='course_create'),
#     path('courses/<int:pk>/', views.CourseDetailView.as_view(), name='course_detail'),
#     path('applications/', views.ApplicationListView.as_view(), name='application_list'),
#     path('applications/apply/<int:course_pk>/', views.ApplicationCreateView.as_view(), name='application_create'),
#     path('applications/<int:pk>/', views.ApplicationDetailView.as_view(), name='application_detail'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/', views.applicant_dashboard, name='applicant_dashboard'),
    # Add other URL patterns as needed
]
