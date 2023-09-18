from django.urls import path

from . import views

urlpatterns = [
    # ex: /tickets/
    path("<int:wr_name>/", views.ticket, name="index"),
    # path("login/", views.login, name="login"),
    path("login/", views.login, name="login"),
    path("", views.home, name="home"),
    path("logout/", views.logout, name="logout"),
]