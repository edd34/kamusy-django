from django.urls import path

from components.translation import views

urlpatterns = [
    path("api/translations/", views.translation_list, name="translation-list"),
    path("api/add-translation/", views.create_translation, name="add-translation"),
    path(
        "api/translations/<int:pk>/",
        views.translation_detail,
        name="translation-detail",
    ),
    path(
        "translations/<str:pattern>/<int:language_src_id>/<int:language_dst_id>/",
        views.find_translations,
        name="translation-find",
    ),
    path(
        "api/get-translation/<int:word_id>/<int:language_src_id>/<int:language_dst_id>/",
        views.get_translation,
        name="translation-get",
    ),
    path(
        "api/get-translation-multi/<str:word_id>/<int:language_src_id>/<int:language_dst_id>/",
        views.get_translation_multi,
        name="translation-get-multi",
    ),
]
