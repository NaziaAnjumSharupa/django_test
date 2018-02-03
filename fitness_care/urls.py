from django.urls import path,re_path
from fitness_care import views
urlpatterns = [
    path("index/",views.index,name="index"),
]