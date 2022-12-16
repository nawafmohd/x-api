from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = "api"

urlpatterns = [
    # path('', views.PostsList.as_view()),          # class base
    path('', views.postsList, name='posts-list'),    # function base
    path('<int:pk>', views.post_detail, name='post_detail'),    # function base
]

# http://127.0.0.1:8000/api.json
urlpatterns = format_suffix_patterns(urlpatterns)