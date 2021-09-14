from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import Poll, Question, Vote
from .serializers import PollSerializer, QuestionSerializer, VoteSerializer


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']
