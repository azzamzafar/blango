from django.urls import path
from blog.api.views import PostList, PostDetail
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
  path("posts/",PostList.as_view(),name="api_post_lsit"),
  path("posts/<int:pk>", PostDetail.as_view(), name="api_post_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)