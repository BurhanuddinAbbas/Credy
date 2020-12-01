"""Credy URL Configuration

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
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from Account import views as acc_views
from Movie import views as mov_views
from Collection import views as coll_views
from Credy import views as cre_views

urlpatterns = [
    path('register/', acc_views.UserCreateAPIView.as_view()),
    path('movies/', mov_views.list_movies),
    path('collection/', coll_views.CollectionViewSet.as_view()),
    path('collection/<uuid>', coll_views.CollectionViewSet.as_view()),
    path('request-count/', cre_views.request_counter),
    path('request-count/reset/', cre_views.request_counter_reset),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
