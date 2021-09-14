from rest_framework import serializers

from .models import Poll, Question, Choice


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


