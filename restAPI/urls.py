from django.urls import path, include

from rest_framework import routers

from restAPI import views


router = routers.DefaultRouter()
router.register(r'measurements', views.MeasurementsViewSet)

# Wire up API using automatic URL routing.
# Additionally including login URLs for browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]