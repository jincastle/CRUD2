from django.urls import path, include
from .views import *

urlpatterns = [
        path('',MoviesView.as_view()),
        path('/actor',ActorView.as_view()),
        ]

