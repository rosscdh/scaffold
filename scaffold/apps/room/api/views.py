from rest_framework import generics

from .serializers import RoomPackageSerializer
from ..models import Room, RoomPackage


class RoomPackagesApiView(generics.ListAPIView):
    queryset = RoomPackage.objects.all()
    serializer_class = RoomPackageSerializer

    def get_queryset(self):
        self.room = Room.objects.get(pk=self.kwargs.get('room_pk'))
        return RoomPackage.objects.filter(room_type=self.room.room_type)


class RoomPackageDetailApiView(generics.RetrieveAPIView,
                               RoomPackagesApiView):
    pass