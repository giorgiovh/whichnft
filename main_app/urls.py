from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('collections/', views.collections_index, name='collections_index'),
    path('collections/<int:collection_id>/', views.collections_detail, name='collections_detail')
]