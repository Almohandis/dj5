from django.urls import path
from content import views

# TEMPLATE TAGGING
app_name = "content"

urlpatterns = [
    # path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("user_login/", views.user_login, name="user_login"),
]
