from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from mailing import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('upload/', views.upload_subscribers, name='upload'),
    path('export/', views.export_subscribers, name='export'),
    path('unsubscribe/', views.unsubscribe_view, name='unsubscribe'),
    path('upload_excel/', views.upload_excel, name='upload_excel'),
    path('export_csv/', views.export_csv, name='export_csv'),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
]