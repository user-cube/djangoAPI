"""djangoAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from app import views
from rest_framework.documentation import include_docs_urls
from rest_framework.permissions import BasePermission
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('items/', views.get_items),
    path('items/<str:name>/', views.get_items_by_name),
    path('items/info/<int:id>', views.get_items_info),
    path('items', views.edit_items),
    path('profile', views.get_user),
    path('encomendas', views.get_user_encomendas),
    path('encomendas/search/<str:name>', views.search_encomendas),
    path('login/', obtain_jwt_token, name="token"),
    path('admin/panel/', views.get_admin_panel),
    path('admin/del/<int:id>', views.deleteItems),
    path('admin/encomendas/', views.get_encomendas_admin),
    path('admin/encomendas/<str:name>', views.search_encomendas_admin),
    path('',
         include_docs_urls(title='XPTO Store API',
                           public=True,
                           authentication_classes=(),
                           permission_classes=([BasePermission])
                           )
         )
]
