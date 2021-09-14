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

    def __str__(self):
        return f'{self.name} : {self.description}'

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


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
        max_length=64,
        verbose_name='Тип вопроса',
        choices=type_question,
        default='text'
    )
    poll = models.ForeignKey(
        Poll,
        on_delete=models.CASCADE,
        related_name='questions'
    )

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Choice(models.Model):
    choice_text = models.CharField(
        max_length=255,
        verbose_name='Текст ответа'
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="choices"
    )

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class Answer(models.Model):
    user = models.IntegerField(verbose_name='id пользователя', null=True)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, verbose_name='Опрос')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, verbose_name='Выбор ответа')
