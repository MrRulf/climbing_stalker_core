from django.urls import path

from restAPI import views


urlpatterns = [
    path('measurementsSets/latest/', views.measurements_sets_latest),
    path('measurementsSets/object/<int:id>', views.measurements_sets_object),
    path('measurementsSets/<int:pk>/', views.measurements_sets_id),
    path('measurementsSets/<int:pk>/details/', views.measurements_sets_id_details),
    path('measurementsSets/', views.measurements_sets),
    path('measurements/latest/', views.measurements_latest),
    path('measurements/object/<int:id>', views.measurements_object),
    path('measurements/<int:pk>/', views.measurements_id),
    path('measurements/', views.measurements)
]