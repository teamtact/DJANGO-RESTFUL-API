from rest_framework import serializers
from games.models import Game


class GameSerializer(serializers.ModelSerializer):
    # We want to display the game cagory's name instead of the id
    game_category = serializers.SlugRelatedField(queryset=GameCategory.objects.all(), slug_field='name')

    class Meta:
        model = Game
        fields = (
            'url',
            'game_category',
            'name',
            'release_date',
            'played')
