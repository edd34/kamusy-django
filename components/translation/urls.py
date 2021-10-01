from django.urls import path
from components.language import views
  
urlpatterns = [
    path('transations/',
         views.translation_list,
         name = 'translation-list'),
    path('translations/<int:pk>/',
         views.translation_detail,
         name = 'translation-detail'),

]
