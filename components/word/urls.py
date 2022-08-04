from django.urls import path
from components.word import views

urlpatterns = [
    path("api/words/", views.word_list, name="word-list"),
    path("api/words/<int:pk>/", views.word_detail, name="word-detail"),
    path(
        "api/find-words/<str:pattern>/<int:language_src_id>/",
        views.find_word,
        name="word-find",
    ),
    path(
        "api/find-words-2/<str:pattern>/<int:language_src_id>/<int:language_dst_id>/",
        views.find_word_v2,
        name="word-find-2",
    ),
    path(
        "api/mixed_word",
        views.mixed_word,
        name="mixed-word",
    ),
]
