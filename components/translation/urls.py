from django.urls import path
from components.translation import views
  
urlpatterns = [
    path('translations/',
         views.translation_list,
         name = 'translation-list'),
    path('translations/<int:pk>/',
         views.translation_detail,
         name = 'translation-detail'),

]
