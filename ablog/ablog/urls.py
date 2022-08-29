"""ablog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include # @Dev
from django.conf import settings # @Dev
from django.conf.urls.static import static # @Dev

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('theblog.urls')), # @Dev
    path('members/', include('django.contrib.auth.urls')), # @Dev
    path('members/', include('members.urls')), # @Dev
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # @Dev