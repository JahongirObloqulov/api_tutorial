from django.urls import path
from . import views
urlpatterns = [
    path('api/', views.SnippetList.as_view()),
    path('api/<int:pk>/', views.SnippetDetail.as_view())
]
