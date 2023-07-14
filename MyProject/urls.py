"""
URL configuration for MyProject project.

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
from django.urls import path
from MyApp import TopicRestApi
from MyApp import ContentRestApi
from MyApp import PostcategoriesApis
from MyApp import StatesRestApi
from MyApp import CityRestApi
from MyApp import LocationRestApi
from MyApp import QualificationsRestApi
from MyApp import SpecializationsRestApi
from MyApp import RolesRestApi



urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/topic', TopicRestApi.TopicApi.as_view()),
    path('api/topic/<int:pk>/', TopicRestApi.TopicUpdateDeleteApi.as_view()),
    path('api/content',ContentRestApi.ContentApi.as_view()),
    # path('api/content/<int:pk>/', TopicRestApi.TopicUpdateDeleteApi.as_view()),
    path('api/role', RolesRestApi.RoleApi.as_view()),
    # path('api/topic/<int:pk>/', TopicRestApi.TopicUpdateDeleteApi.as_view()),
    # path('api/topic', TopicRestApi.TopicApi.as_view()),
    # path('api/topic/<int:pk>/', TopicRestApi.TopicUpdateDeleteApi.as_view()),
    # path('api/topic', TopicRestApi.TopicApi.as_view()),
    # path('api/topic/<int:pk>/', TopicRestApi.TopicUpdateDeleteApi.as_view()),
    # path('api/topic', TopicRestApi.TopicApi.as_view()),
    # path('api/topic/<int:pk>/', TopicRestApi.TopicUpdateDeleteApi.as_view()),
    # path('api/topic', TopicRestApi.TopicApi.as_view()),
    # path('api/topic/<int:pk>/', TopicRestApi.TopicUpdateDeleteApi.as_view()),
]
