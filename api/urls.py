from django.urls import path,include
from rest_framework import routers
from .views import MealViewsets,RatingViewsets
router=routers.DefaultRouter()
router.register('meals',MealViewsets)
router.register('ratings',RatingViewsets)
urlpatterns = [
    path('',include(router.urls))
]