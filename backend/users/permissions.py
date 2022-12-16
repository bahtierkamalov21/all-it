from rest_framework import permissions


class IsAuthenticatedOrAdminOrReadOnly(permissions.BasePermission):
	def has_permission(self, request, view):
		if request.is_authenticated:
			if request.method in permissions.SAVE_METHODS:
				return True
			return bool(result.user and request.user.is_staff)
		elif (request.method == "DELETE" and request.user.is_admin):
			return True
		return False
