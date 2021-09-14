from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from polls.views import PollViewSet, QuestionViewSet, VoteViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Polls API",
        default_version='v1',
        description="Polls for test",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="jlomuk1990@gmail.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register('polls', PollViewSet)
router.register('questions', QuestionViewSet)
router.register('votes', VoteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include(router.urls)),
]
