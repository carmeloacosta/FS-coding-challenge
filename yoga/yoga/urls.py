"""yoga URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views.user import UserView
from .views.posture import PostureView
from .views.posture_list import PostureListView
from .views.default import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='accounts/login'), name="home"),
    path('user/add', UserView.as_view(), name="user_add"),
    path('posture/add', PostureView.as_view(), name="posture_add"),
    path('posture/get', PostureView.as_view(), name="posture_get"),
    path('posture/get_all', PostureListView.as_view(), name="posture_get_all"),
    path('accounts/', include('django.contrib.auth.urls'), name="login"),
]

urlpatterns += staticfiles_urlpatterns()

handler404 = handler404
handler500 = handler500
