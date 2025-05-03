from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Review
from .serializers import ReviewSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/reviews',
        'GET /api/reviews/:id'
    ]
    return Response(routes)

@api_view(['GET'])
def getReviews(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getReview(request, pk):
    review = Review.objects.get(id=pk)
    serializer = ReviewSerializer(review, many=False)
    return Response(serializer.data)