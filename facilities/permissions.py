from rest_framework import permissions

class AdminPutOrAnonReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method == 'PUT':
            return request.user and request.user.is_staff

        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method == 'PUT':
            return request.user and request.user.is_staff

        return False