from django.urls import path
from . import views


app_name = "core"

urlpatterns = [
    # path("", views.index),
    path("", views.index, name="index"),  # URL Reverse를 위한 URL pattern명 지정
]
