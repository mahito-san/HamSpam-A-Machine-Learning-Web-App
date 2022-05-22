from django.urls import path
from .import views

# app_name = 'comment_app'


urlpatterns = [
    path('', views.index, name='comment_app-index'),
    path('predictions/', views.predictions, name='comment_app-predictions'),
]