from django.urls import path
from components.word import views

urlpatterns = [
    path('words/',
         views.word_list,
         name='word-list'),
    path('words/<int:pk>/',
         views.word_detail,
         name='word-detail'),
    path('find-words/<str:pattern>/<int:language_src_id>/',
         views.find_word,
         name='word-find'),
]
