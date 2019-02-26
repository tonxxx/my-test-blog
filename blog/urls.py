from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), # BAD STYLE!! SHOULD USE CLASS-BASED N GENERIC N SHIT LIKE @ DJ TUTORIAL!!!
    path('post/<str:title>/', views.post_detail, name='post_detail'),
]
