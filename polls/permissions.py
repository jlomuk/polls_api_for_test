import datetime
from rest_framework.permissions import BasePermission


class PollPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        view.queryset = view.queryset.filter(
            end_date__gte=datetime.datetime.now()
        )
        print(datetime.datetime.now())
        if request.method == 'GET':
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)


class QuestionPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)
