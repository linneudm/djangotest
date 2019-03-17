"""djangotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import include
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from djangotest.core import urls as core_urls

#Viewsets
from djangotest.product.api.viewsets import ProductViewSet, OperationViewSet


#Registro das rotas
router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, base_name='Product')
router.register(r'operations', OperationViewSet, base_name='Operation')

urlpatterns = [
    path('', include(router.urls)),
    path('home/', include(core_urls, namespace='core')),
    path('api-token-auth/', obtain_auth_token),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
