from django.urls import path
from components.language import views

urlpatterns = [
    path("languages/", views.language_list, name="language-list"),
    path("add-language/", views.add_language, name="add-language"),
    #     path('languages/<int:pk>/',
    #          views.language_detail,
    #          name = 'language-detail'),
]
