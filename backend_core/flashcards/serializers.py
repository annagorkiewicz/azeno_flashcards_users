from rest_framework.serializers import ModelSerializer
from .models import FlashCard


class FlashCardSerializer(ModelSerializer):
    class Meta:
        model = FlashCard
        fields = ('id', 'author', 'category', 'difficulty', 'rating', 'tags', 'decks', 'question', 'answer')
