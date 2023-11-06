from django.utils import timezone
from rest_framework.permissions import IsAuthenticated

from main_page.models import UserActivity


class CustomIsAuthenticated(IsAuthenticated):
    def has_permission(self, request, view):
        user_activity, _ = UserActivity.objects.get_or_create(user=request.user)
        user_activity.last_request = timezone.now()
        user_activity.save()

        return bool(request.user and request.user.is_authenticated)
