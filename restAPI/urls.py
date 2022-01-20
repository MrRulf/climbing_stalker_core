from django.urls import path

from restAPI import views


urlpatterns = [
    path('measurementsSets/latest/', views.measurementsSetsLatest),
    path('measurementsSets/<int:pk>/', views.measurementsSetsId),
    path('measurementsSets/', views.measurementsSets),
    path('measurements/latest/', views.measurementsLatest),
    path('measurements/<int:pk>/', views.measurementsId),
    path('measurements/', views.measurements)
]