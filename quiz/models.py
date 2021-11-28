from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Quiz(models.Model):
    """
        Stores a single Quiz entry, related to `auth.User` Model.
    """
    id = models.BigAutoField(primary_key=True, unique=True)

    title = models.CharField(max_length=120,
                             default=_('One More Quiz'),
                             verbose_name=_('Quiz Title'))
    description = models.CharField(max_length=255,
                                   default=_('New Quiz Description'),
                                   verbose_name=_('Quiz Description'))
    start_date = models.DateTimeField()
    expiration_date = models.DateTimeField()

    owner = models.ForeignKey(User, on_delete=models.CASCADE, to_field='id')

    class Meta:
        db_table = 'quizzes'
        verbose_name = _('Quiz')
        verbose_name_plural = _('Quizzes')

    def __str__(self):
        return self.title


class BaseQA(models.Model):
    created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('Last Updated'), auto_now=True)

    class Meta:
        abstract = True


class Question(BaseQA):
    """
        Store a single Question entry, related to 'Quiz' Model
    """
    TYPE_OF_QUESTION = [
        (0, _('Text')),
        (1, _('Single Choice')),
        (2, _('Multiple Choice'))
    ]

    id = models.BigAutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=255, verbose_name=_('Question Title'))
    question_type = models.IntegerField(verbose_name=_('Question Type'), choices=TYPE_OF_QUESTION, default=0)

    quiz = models.ForeignKey(Quiz, related_name='question', on_delete=models.CASCADE, to_field='id')

    class Meta:
        db_table = 'questions'
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')

    def __str__(self):
        return self.title


class Answer(BaseQA):
    """
        Store a single Answer entry, related to 'Question' Model
    """
    id = models.BigAutoField(primary_key=True, unique=True)
    answer_text = models.CharField(max_length=255, verbose_name=_('Answer Text'))
    is_correct = models.BooleanField(default=False)

    question = models.ForeignKey(Question, related_name='answer', on_delete=models.CASCADE, to_field='id')

    class Meta:
        db_table = 'answers'
        verbose_name = _('Answer')
        verbose_name_plural = _('Answers')

    def __str__(self):
        return self.answer_text
