from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("add_new_image/", views.add_new_image, name="add_new_image"),
    path("get_all_posts/", views.get_all_posts, name="get_all_posts"),
]
