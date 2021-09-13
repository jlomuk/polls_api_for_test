from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from polls.views import PollViewSet, QuestionViewSet, ChoiceViewSet


router = DefaultRouter()
router.register('polls', PollViewSet)
router.register('questions', QuestionViewSet)
router.register('choices', ChoiceViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
