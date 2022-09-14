from django.urls import path,include
from blog import views
from blog.api_views import post_list, post_detail

urlpatterns = [
  path("",views.index,name="index"),
  path("blog/<int:pk>",views.post_detail,name="post_detail"),
  path("ip/",views.get_ip),
  path("profile/",include('blango_auth.urls')),
  
]
