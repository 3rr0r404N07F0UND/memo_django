from django.contrib import admin
from django.urls import path
from api_app import views

urlpatterns = [
    path("user/id/", views.user_id_api),
    path("user/pw/", views.user_pw_api),
    path("delete/", views.delete_memo),
    path("create/", views.create_memo),
    path("shows/", views.show_list),
    path("get/memo/", views.get_memo),
    path("pk/memo/", views.get_pk),
    path("mode/pk/", views.mode_pk),
    path("create/account/", views.create_account),
    path("create/account/post", views.create_account_post),
]
