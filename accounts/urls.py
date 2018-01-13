from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from .views import *

app_name = 'accounts'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('employer-register/', EmployerRegisterView.as_view(), name='employer-register'),
    path('profile/<str:username>', ProfileView.as_view(), name='profile'),
    path('profile/update/', UpdateProfileView.as_view(), name='update'),
    path('profile/employer-update/', UpdateEmployerView.as_view(), name='employer-update'),
    path('profile/employer-jobs/', EmployerJobsView.as_view(), name='employer-jobs'),


]
