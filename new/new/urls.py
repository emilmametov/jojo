"""new URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path
from newpols import views
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
	path('', views.main_page_view, name='home'),
	path('signup/', views.SignUp.as_view(), name='signup'),
    path('pars/', views.requst, name = 'requst'),
    path('sport/',views.sport, name = 'sport')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

