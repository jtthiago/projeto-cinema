from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, BookingViewSet, ActionLogViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'logs', ActionLogViewSet)  # Adiciona a rota /api/logs/

urlpatterns = [
    path('', include(router.urls)),
]
