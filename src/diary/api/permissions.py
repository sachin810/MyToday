from rest_framework.permissions import BasePermission


class IsOwnerOrAdmin(BasePermission):
    """
    Custom permission to only allow owners of an object to see and edit it.
    Admin users however have access to all.
    """
    def has_object_permission(self, request, view, obj):
        # Permissions are only allowed to the owner of the snippet
        if request.user.is_staff:
            return True
        return obj.owner == request.user
