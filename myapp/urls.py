from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('loginaction', views.loginaction),
    path('signup', views.signup),
    path('signupaction', views.signupaction),
    path('addpodcast/', views.addpodcast, name='addpodcast'),
    path('podcast/<int:podcast_id>/', views.player, name='player'),
    path('about',views.about),
    path('profile',views.profile),
    path('library',views.library),
    path('update',views.update),
]
