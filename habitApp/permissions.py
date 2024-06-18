from rest_framework import permissions

"""Проверка на собственника"""


class IsOwnerHabit(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
