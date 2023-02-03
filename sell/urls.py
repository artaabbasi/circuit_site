from django.urls import path
from . import views
urlpatterns = [
    path('items/', views.items),
    path('item/<int:item_id>/', views.item),
    path('tags/', views.tags),
    path('tag/<int:item_id>/', views.tag),
]
