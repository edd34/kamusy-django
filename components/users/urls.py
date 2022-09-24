from django.urls import path

from components.users import views

urlpatterns = [
    path("api/sign-ign/", views.create_user, name="create_user"),
]
