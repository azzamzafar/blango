from django.urls import path
from blango_auth import views
urlpatterns = [
  path("",views.profile,name="profile")
]