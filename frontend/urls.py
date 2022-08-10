from django.urls import path
from frontend.views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
]
