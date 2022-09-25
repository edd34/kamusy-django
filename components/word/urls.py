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
        "api/find-words-3/<str:pattern>/<str:language_src>/<str:language_dst>/",
        views.find_word_by_name,
        name="word-find-3",
    ),
    path(
        "api/mixed_word/<str:language>/",
        views.mixed_word,
        name="mixed-word",
    ),
    path(
        "api/words_multi/<str:pattern>/<int:language_src_id>/<int:language_dst_id>/",
        views.words_multi,
        name="words-multi",
    ),
]
