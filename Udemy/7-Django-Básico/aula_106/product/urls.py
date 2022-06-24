from django.urls import path
from . import views

# /blogs
urlpatterns = [
    path('', views.method),

]
