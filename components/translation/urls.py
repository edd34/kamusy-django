from django.urls import path
from components.translation import views

urlpatterns = [
    path('translations/',
         views.translation_list,
         name='translation-list'),
    path('translations/<int:pk>/',
         views.translation_detail,
         name='translation-detail'),
    path('translations/<str:pattern>/<int:language_src_id>/<int:language_dst_id>/',
         views.find_translations,
         name='translation-find'),
    path('get-translation/<int:word_id>/<int:language_src_id>/<int:language_dst_id>/',
         views.get_translation,
         name='translation-get'),
]
