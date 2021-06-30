from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        full_path = request.get_full_path()
        resource = full_path.split("/")[3]

        if resource == "usuarios":
            return obj == request.user

        return obj.user == request.user


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
