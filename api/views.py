from django.shortcuts import render
from .serializers import MealSerializer,RatingSerializer
from .models import Meal,Rating
from rest_framework import viewsets,status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
# Create your views here.
class MealViewsets(viewsets.ModelViewSet):
    queryset=Meal.objects.all()
    serializer_class=MealSerializer

    @action(methods=['post'],detail=True)
    def rate_meal(self,request,pk=None):
        if 'stars' in request.data:
            #create or update
            meal=Meal.objects.get(pk=pk)
            stars=request.data['stars']
            username=request.data['user']
            user=User.objects.get(username=username)

            try:
                #updata only
                rating=Rating.objects.get(user=user.id,meal=meal.id)
                rating.stars=stars
                serializer=RatingSerializer(rating,many=False)
                rating.save()
                json={
                    'messege':'rating meal has been updated',
                    'result':serializer.data
                }
                return Response(data=json,status=status.HTTP_202_ACCEPTED)
            except:
                #create only 
                rating=Rating.objects.create(user=user.id,meal=meal.id)
                rating.stars=stars
                serializer=RatingSerializer(rating,many=False)
                rating.save()
                json={
                    'messege':'rating meal has been created',
                    'result':serializer.data
                }
                return Response(data=json,status=status.HTTP_201_CREATED)
        else:
            json={'message':'stars not provided'}
            return Response(json,status=status.HTTP_400_BAD_REQUEST)

class RatingViewsets(viewsets.ModelViewSet):
    queryset=Rating.objects.all()
    serializer_class=RatingSerializer
