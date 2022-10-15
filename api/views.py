from django.shortcuts import render
from .serializers import MealSerializer,RatingSerializer
from .models import Meal,Rating
from rest_framework import viewsets
# Create your views here.
class MealViewsets(viewsets.ModelViewSet):
    queryset=Meal.objects.all()
    serializer_class=MealSerializer

class RatingViewsets(viewsets.ModelViewSet):
    queryset=Rating.objects.all()
    serializer_class=RatingSerializer
