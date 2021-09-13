from django.db import models


class Poll(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Название опроса',
    )
    created_data = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now=True,
    )
    end_data = models.DateTimeField(
        verbose_name='Дата окончания'
    )
    description = models.TextField(
        verbose_name='Описание опроса'
    )


class Question(models.Model):
    type_question = (
        ('text', 'Текст'),
        ('one_choiсe', 'Один ответ'),
        ('multi_choices', 'Несколько ответов'),
    )

    question_text = models.CharField(
        max_length=255,
        verbose_name='Вопрос',
    )
    type = models.CharField(
        verbose_name='Тип вопроса',
        choices=type_question,
        default='text'
    )
    poll = models.ForeignKey(
        Poll,
        on_delete=models.CASCADE,
        related_name='questions'
    )


class Choice(models.Model):
    choice_text = models.CharField(
        max_length=255,
        verbose_name='Текст ответа'
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
    )


class Answer(models.Model):
    user = models.IntegerField(verbose_name='id пользователя', null=True)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
