from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import Poll, Question, Vote
from .serializers import PollSerializer, QuestionSerializer, VoteSerializer
from .permissions import QuestionPermission, PollPermission


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [PollPermission]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [QuestionPermission]


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']
    http_method_names = ('get', 'post')
