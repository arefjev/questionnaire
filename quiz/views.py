from rest_framework import generics

from .models import Quiz
from .serializers import QuizSerializer


class QuizView(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()
