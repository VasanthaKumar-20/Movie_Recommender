from rest_framework.views import APIView
from rest_framework.response import Response

# Static dataset of movies
MOVIES = [
    {"title": "The Goat", "genre": "Sci-Fi", "rating": 8.8},
    {"title": "Leo", "genre": "Action", "rating": 9.0},
    {"title": "Interstellar", "genre": "Sci-Fi", "rating": 8.6},
    {"title": "The Godfather", "genre": "Crime", "rating": 9.2},
    {"title": "Pulp Fiction", "genre": "Crime", "rating": 8.9},
    {"title": "The Shawshank Redemption", "genre": "Drama", "rating": 9.3},
    {"title": "Fight Club", "genre": "Drama", "rating": 8.8},
]

class MovieRecommendationAPIView(APIView):
    def get(self, request):
        genre = request.query_params.get("genre", None)  # Get genre from query params

        # Filter movies by genre if provided, otherwise return all
        if genre:
            filtered_movies = [movie for movie in MOVIES if movie["genre"].lower() == genre.lower()]
            return Response(filtered_movies)
        return Response(MOVIES)
