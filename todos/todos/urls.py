"""todos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
import debug_toolbar
from django.contrib import admin
from django.urls import path, include

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name="home"),
    path('user/todos', views.user_detail, name="todos-for-user"),
    path('accounts/', include('registration.backends.simple.urls')),
    path('__debug__', include(debug_toolbar.urls)),
    path('mytodos/', views.user_detail, name="mytodos"),
    path('category/<int:pk>/', views.category_detail, name="category-detail"),
    path('api/todos', views.list_todos_json, name="list-todos-json"),
    path('api/user/todos', views.todos_by_user_json, name="todos-by-user-json"),
] 

#TODO make url for listing user's personal Todos


