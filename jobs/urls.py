from django.urls import path, include
from . import views
from .views import *


app_name = 'jobs'
urlpatterns = [
    # Home
    path('', HomeView.as_view(), name='home'),
    # Browse Jobs
    path('browse/', BrowseView.as_view(), name='browse'),
    path('job/<int:pk>', BrowseDetailView.as_view(), name='detail'),
    # Job Search
    path('search/', JobSearchView.as_view(), name='search'),
    path('create-job/', CreateJobView.as_view(), name='create-job'),
    path('delete-job/<str:pk>', DeleteJobView.as_view(), name='delete-job'),


]
