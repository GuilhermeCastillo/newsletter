from django.urls import path
from .views import  DashboardHomeView, NewsletterDashboardHomeView

app_name = "dashboard"

urlpatterns = [
    path('', DashboardHomeView.as_view(), name="home"),
    path('list/', NewsletterDashboardHomeView.as_view(), name="list"),
]
