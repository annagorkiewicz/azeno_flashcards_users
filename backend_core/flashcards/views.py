from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import FlashCard
from .serializers import FlashCardSerializer


class FlashCardView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = FlashCard.objects.all()
    serializer_class = FlashCardSerializer

    def get_queryset(self):
        rating = self.request.query_params.get('rating', 0)

        return FlashCard.objects.filter(rating__gte=rating)


class FlashCardItemView(RetrieveUpdateDestroyAPIView):
    queryset = FlashCard.objects.all()
    serializer_class = FlashCardSerializer
