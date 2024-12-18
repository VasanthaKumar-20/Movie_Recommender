from django.urls import path
from .views import MovieRecommendationAPIView

urlpatterns = [
    path('recommendations/', MovieRecommendationAPIView.as_view(), name='movie-recommendations'),
]
