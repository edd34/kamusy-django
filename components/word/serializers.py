from rest_framework import serializers
from components.word.models import Word


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = "__all__"
