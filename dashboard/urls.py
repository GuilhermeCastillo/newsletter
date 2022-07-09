from django.urls import path
from .views import  DashboardHomeView, NewsletterDashboardHomeView, NewsletterCreateView

app_name = "dashboard"

urlpatterns = [
    path('', DashboardHomeView.as_view(), name="home"),
    path('list/', NewsletterDashboardHomeView.as_view(), name="list"),
    path('create/', NewsletterCreateView.as_view(), name="create"),
]
