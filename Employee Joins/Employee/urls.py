"""
URL configuration for Employee project.

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

from django.urls import path    
from Employee_app.views import (department_list_create_update_delete,
                                position_list_create_update_delete,
                                employee_list_create_update_delete,
                                address_list_create,
                                salary_list_create,
                                employees_in_specific_position_with_department,
                                employees_in_specific_department,
                            )

urlpatterns = [

    path('departments/', department_list_create_update_delete, name='department_list_create_update_delete'),
    path('departments/<int:pk>/', department_list_create_update_delete, name='department-detail'),

    path('positions/', position_list_create_update_delete, name='position-list-create-update-delete'),
    path('positions/<int:pk>/', position_list_create_update_delete, name='position-detail'),
    
    path('employees/', employee_list_create_update_delete, name='employee-list-create-update-delete'),
    path('employees/<int:pk>/', employee_list_create_update_delete, name='employee-detail'),

    path('addresses/', address_list_create, name='address-list-create'),
    path('salary/', salary_list_create, name='salary-list-create'),

    path('employees_in_specific_position_with_department/',employees_in_specific_position_with_department,name='employees_in_specific_position_with_department'),

    path('employees_in_specific_department/',employees_in_specific_department,name='employees_in_specific_department'),

]

