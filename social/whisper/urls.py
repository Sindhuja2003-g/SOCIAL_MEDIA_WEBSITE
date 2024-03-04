from django.urls import path
from .views import *

app_name="whisper"
urlpatterns=[
    path("",dashboard,name="dashboard"),
    path("profile_list/",profile_list,name="profile_list"),
    path("profile/<int:pk>",profile,name="profile"),
    path("dashboard/", dashboard, name="dashboard")
]