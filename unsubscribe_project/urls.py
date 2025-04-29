from django.contrib import admin
from django.urls import path
from mailing.views import unsubscribe_view, upload_excel  # ← добавляем upload_excel
from mailing import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('unsubscribe/', unsubscribe_view, name='unsubscribe'),
    path('upload/', upload_excel, name='upload_excel'),  # ← новая строка
]

from django.contrib.auth import views as auth_views

urlpatterns += [
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
]

from mailing.views import export_csv  # ← добавь

urlpatterns += [
    path("export/", export_csv, name="export_csv"),  # ← новая строка
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('upload/', views.upload_subscribers, name='upload'),
    path('export/', views.export_subscribers, name='export'),
]