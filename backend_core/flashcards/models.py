from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class DifficultyLevel(models.Model):
    name = models.CharField(max_length=20)
    value = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=24)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        tag = Tag.objects.filter(name=self.name.lower())
        self.name = self.name.lower()

        if not tag:
            return super().save(force_insert, force_update, using, update_fields)

        return tag


class Feature(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s')
    category = models.CharField(max_length=32, null=True)
    difficulty = models.ForeignKey('DifficultyLevel', on_delete=models.CASCADE, related_name='%(class)s')
    rating = models.IntegerField(default=0, blank=True)
    tags = models.ManyToManyField('Tag', related_name='%(class)s')

    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Deck(Feature):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class FlashCard(Feature):
    decks = models.ManyToManyField('Deck', related_name='flashcards')
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return f'Card: {self.pk}'
