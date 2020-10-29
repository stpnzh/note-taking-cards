from django.urls import path
from notes import views

urlpatterns = [
  path('notes/', views.note_list)
]