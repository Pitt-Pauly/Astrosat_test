from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from rest_framework import mixins, generics
from rest_framework import viewsets, status
from rest_framework.permissions import IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, AllowAny
from rest_framework.response import Response

from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Facility
from .serializers import FacilitySerializer
from .permissions import AdminPutOrAnonReadOnly

class FacilitiesBatchCreate(generics.CreateAPIView):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    permission_classes = [ IsAdminUser ]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class FacilitiesDetail(generics.RetrieveUpdateAPIView):
    serializer_class = FacilitySerializer
    permission_classes = [ AdminPutOrAnonReadOnly ]

    def get_queryset(self):
        """
        Filter queryset to include only active facilities for anonymous users.
        Show full queryset to admins.
        """
        user = self.request.user
        if user.is_authenticated and user.is_staff :
            return Facility.objects.all()

        return Facility.objects.filter(status="Active")

class FacilitiesList(generics.ListAPIView):
    serializer_class = FacilitySerializer
    permission_classes = [ AllowAny ]

    def get_queryset(self):
        """
        Filter queryset to include only active facilities for anonymous users.
        Show full queryset to admins.
        """
        user = self.request.user
        if user.is_authenticated and user.is_staff:
            return Facility.objects.all()

        return Facility.objects.filter(status="Active")
