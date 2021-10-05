from rest_framework import serializers
from components.translation.models import Translation


class TranslationSerializer(serializers.ModelSerializer):
    word_source_name = serializers.CharField(source='word_source.name')
    word_destination_name = serializers.CharField(
        source='word_destination.name')
    language_source_name = serializers.CharField(source='language_source.name')
    language_destination_name = serializers.CharField(
        source='language_destination.name')

    class Meta:
        model = Translation
        fields = "__all__"
