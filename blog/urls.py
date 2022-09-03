from django.urls import path,include
from blog import views
urlpatterns = [
  path("",views.index,name="index"),
  path("blog/<int:pk>",views.post_detail,name="post_detail"),
  path("profile/",include('blango_auth.urls'))
]