from rest_framework.permissions import BasePermission


class IsAuthorOrModeratorOrAdminOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.method == 'GET' or

            request.method == 'POST' and
            request.user and
            request.user.is_authenticated or
            
            request.method in ('PUT', 'PATCH', 'DELETE') and
            request.user and
            (request.user.is_superuser or
            request.user.is_staff or
            request.user.is_authenticated and
            request.user.role in ('admin', 'moderator')) or
            (request.user == obj.author)
        )

