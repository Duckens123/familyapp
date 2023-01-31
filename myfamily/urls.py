from django.urls import path
from . import views

urlpatterns = [
    path('',views.getMember),
    path('post/',views.postMember),
]