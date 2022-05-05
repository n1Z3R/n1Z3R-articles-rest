from rest_framework import permissions


class IsOwnerOrAuthenticatedOrReadOnly(permissions.BasePermission):
    '''Permission class which disable 'CREATE' for unauthenticated users and disable
    'UPDATE','DELETE' for users which didn't create current object (READ for all)'''

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_authenticated)
