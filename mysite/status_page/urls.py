from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('submit/', views.submit, name='submit'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('error/', views.error, name='error'),  # Add this line
]
