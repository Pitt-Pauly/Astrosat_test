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
