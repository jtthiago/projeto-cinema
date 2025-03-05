from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, BasePermission
from .permissions import IsStaffUser
from .serializers import MovieSerializer, BookingSerializer
from movies.models import Movie
from booking.models import Booking
from logs.models import ActionLog
from .serializers import ActionLogSerializer
from rest_framework.permissions import IsAdminUser


# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated, IsStaffUser]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticated()]
        return [IsAuthenticated(), IsStaffUser()] 


class ActionLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ActionLog.objects.all().order_by('-timestamp')  # Logs mais recentes primeiro
    serializer_class = ActionLogSerializer
    permission_classes = [IsAdminUser]
# Permissão personalizada para funcionários

class IsStaffUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff