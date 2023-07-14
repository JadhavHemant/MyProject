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
from MyApp import GendersRestApi
from MyApp import DesignationsRestApi
from MyApp import UserDetailsRestApi
from MyApp import QualiRestApi
from MyApp import UserExperianceRestApi
from MyApp import UserProfessionalExpertiseRestApi

urlpatterns = [
    
    path('api/topic', TopicRestApi.TopicApi.as_view()),
    path('api/topic/<int:pk>/', TopicRestApi.TopicUpdateDeleteApi.as_view()),
    
    path('api/content',ContentRestApi.ContentApi.as_view()),
    path('api/content/<int:pk>/', ContentRestApi.ContentUpdateDeleteApi.as_view()),
    
    path('api/postcate', PostcategoriesApis.PostCategoryApi.as_view()),
    path('api/postcate/<int:pk>/', PostcategoriesApis.PostCategoryUpdateDeleteApi.as_view()),
    
    path('api/state', StatesRestApi.StateApi.as_view()),
    path('api/state/<int:pk>/', StatesRestApi.StateUpdateDeleteApi.as_view()),
   
    path('api/city', CityRestApi.CityApi.as_view()),
    path('api/city/<int:pk>/', CityRestApi.CityUpdateDeleteApi.as_view()),
   
    path('api/location', LocationRestApi.LocationApi.as_view()),
    path('api/location/<int:pk>/', LocationRestApi.LocationUpdateDeleteApi.as_view()),
    
    path('api/quali', QualificationsRestApi.QualiApi.as_view()),
    path('api/quali/<int:pk>/', QualificationsRestApi.QualiUpdateDeleteApi.as_view()),
    
    path('api/specialzation', SpecializationsRestApi.SpecializationApi.as_view()),
    path('api/specialzation/<int:pk>/', SpecializationsRestApi.SpecializationUpdateDeleteApi.as_view()), 
    
    path('api/role', RolesRestApi.RoleApi.as_view()),
    path('api/role/<int:pk>/', RolesRestApi.RoleUpdateDeleteApi.as_view()),
    
    path('api/gender', GendersRestApi.GendedrApi.as_view()),
    path('api/gender/<int:pk>/', GendersRestApi.GendedrUpdateDeleteApi.as_view()),
    
    path('api/desig', DesignationsRestApi.DesignationApi.as_view()),
    path('api/desig/<int:pk>/', DesignationsRestApi.DesignationUpdateDeleteApi.as_view()),

    path('api/userdetails', UserDetailsRestApi.UserDetailsApi.as_view()),
    path('api/userdetails/<int:pk>/', UserDetailsRestApi.UserDetailsUpdateDeleteApi.as_view()), 
    
    path('api/userquali', QualiRestApi.QualiUserApi.as_view()),
    path('api/userquali/<int:pk>/', QualiRestApi.QualiUserUpdateDeleteApi.as_view()),
    
    path('api/userexperiance', UserExperianceRestApi.UserExperianceApi.as_view()),
    path('api/userexperiance/<int:pk>/', UserExperianceRestApi.UserExperianceUpdateDeleteApi.as_view()),
    
    path('api/userproexp', UserProfessionalExpertiseRestApi.UserProfessionalExpertiseApi.as_view()),
    path('api/userproexp/<int:pk>/', UserProfessionalExpertiseRestApi.UserProfessionalExpertiseUpdateDeleteApi.as_view()),
     
    # path('api/', UserProfessionalExpertiseRestApi.UserProfessionalExpertiseApi.as_view()),
    # path('api/userexperiance/<int:pk>/', UserProfessionalExpertiseRestApi.UserProfessionalExpertiseUpdateDeleteApi.as_view()),
     
    
    
    
]
