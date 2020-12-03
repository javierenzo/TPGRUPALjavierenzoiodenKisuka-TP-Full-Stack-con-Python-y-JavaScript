from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("prueba", views.inicio, name="inicio"),
    path("login2", views.login_view2, name="login2"),
    path("logout2", views.logout_view, name="logout2")
]
