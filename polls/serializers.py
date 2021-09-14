from rest_framework import serializers

from .models import Poll, Question, Choice, Answer, Vote


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'choice_text')
        read_only_fields = ('id',)


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, required=False)

    class Meta:
        model = Question
        fields = ('id', 'poll', 'question_text', 'type', 'choices')
        read_only_fields = ('id',)

    def create(self, validated_data):
        choices = validated_data.pop('choices')
        question = super().create(validated_data)
        Choice.objects.bulk_create([
            Choice(
                question=question,
                **choice
            ) for choice in choices
        ])
        return question

    def update(self, instance, validated_data):
        choices = validated_data.pop('choices', [])
        instance.choices.all().delete()
        Choice.objects.bulk_create([
            Choice(
                question=instance,
                **choice
            ) for choice in choices
        ])
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class PollSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = ('id', 'name', 'created_data', 'end_data', 'description', 'questions')
        read_only_fields = ('id',)


class AnswerSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(read_only=True)

    class Meta:
        model = Answer
        fields = ('question', 'choice')
        read_only_fields = ('id',)


class VoteSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)
    poll_name = serializers.SerializerMethodField(read_only=True)

    def get_poll_name(self, obj):
        return obj.poll.name

    class Meta:
        model = Vote
        fields = ('id', 'user', 'poll', 'poll_name', 'answers')

    def create(self, validate_data):
        answers = validate_data.pop('answers')
        vote = super().create(validate_data)
        Answer.objects.bulk_create([
            Answer(vote=vote, **answer) for answer in answers
        ])
        return vote
