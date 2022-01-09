import authnapp.views as authnapp
from django.urls import path

app_name = "authnapp"

urlpatterns = [
    path("login/", authnapp.login, name="login"),
    path("logout/", authnapp.logout, name="logout"),
]
