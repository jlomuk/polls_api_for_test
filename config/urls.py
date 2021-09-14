from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from polls.views import PollViewSet, QuestionViewSet


router = DefaultRouter()
router.register('polls', PollViewSet)
router.register('questions', QuestionViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
