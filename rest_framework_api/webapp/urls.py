from django.urls import path, re_path, include

# ----------- import viewe ------------#
from webapp import views


urlpatterns = [
    path("api/v1.0/mbti", views.MBTIAPIView.as_view(), name="MBTIAPIView"),
]
