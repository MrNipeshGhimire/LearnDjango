from django.urls import path
from .views.main_view import home,single_blog,edit_blog,create_blog
from .views.auth_view import register,login

urlpatterns = [
 path("",home, name="home"),
 path("register/",register, name="register"),
 path("login/",login, name="login"),
 path("create/",create_blog),
 path("edit/",edit_blog),
 path("single/",single_blog)
]