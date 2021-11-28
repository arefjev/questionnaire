# Generated by Django 2.2.10 on 2021-11-27 23:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(default='One More Quiz', max_length=120, verbose_name='Quiz Title')),
                ('description', models.CharField(default='New Quiz Description', max_length=255, verbose_name='Quiz Description')),
                ('start_date', models.DateTimeField()),
                ('expiration_date', models.DateTimeField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Quiz',
                'verbose_name_plural': 'Quizzes',
                'db_table': 'quizzes',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=255, verbose_name='Question Title')),
                ('question_type', models.IntegerField(choices=[(0, 'Text'), (1, 'Single Choice'), (2, 'Multiple Choice')], default=0, verbose_name='Question Type')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='quiz.Quiz')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
                'db_table': 'questions',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('answer_text', models.CharField(max_length=255, verbose_name='Answer Text')),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='quiz.Question')),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': 'Answers',
                'db_table': 'answers',
            },
        ),
    ]
