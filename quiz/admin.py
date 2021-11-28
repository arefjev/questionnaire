from django.contrib import admin
from . import models


@admin.register(models.Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'description',
        'start_date',
        'expiration_date'
    ]


class AnswerInlineModel(admin.TabularInline):
    model = models.Answer
    fields = [
        'answer_text',
        'is_correct',
        'question'
    ]


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'question_type',
        'quiz'
    ]
    list_display = [
        'id',
        'title',
        'question_type',
        'quiz'
    ]
    inlines = [
        AnswerInlineModel,
    ]
