from django.urls import path
from Dashboard import views

urlpatterns = [
    path("", views.news, name="news"),
    path("component/", views.component, name="component"),
    path("vehicle/", views.vehicle, name="vehicle"),
    path("overview/", views.overview, name="overview"),
    path("detail/<str:wp_id>/", views.details, name="details"),
]