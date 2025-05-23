from django.contrib import admin
from django.urls import path
from mailing import views
from django.contrib.auth import views as auth_views
from mailing.views import test_error_logging

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('unsubscribe/', views.unsubscribe_view, name='unsubscribe'),
    path('upload/', views.upload_subscribers, name='upload'),
    path('export/', views.export_subscribers, name='export_subscribers'),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("test-error/", test_error_logging),
]