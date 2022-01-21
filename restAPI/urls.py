from django.urls import path

from restAPI import views


urlpatterns = [
    path('measurementsSets/latest/', views.measurements_sets_latest),
    path('measurementsSets/<int:pk>/', views.measurements_sets_id),
    path('measurementsSets/', views.measurements_sets),
    path('measurements/latest/', views.measurements_latest),
    path('measurements/<int:pk>/', views.measurements_id),
    path('measurements/', views.measurements)
]