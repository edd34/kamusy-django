from rest_framework import serializers
from components.translation.models import Translation


class GetTranslationSerializer(serializers.ModelSerializer):
    word_source_name = serializers.CharField(source="word_source.name")
    word_destination_name = serializers.CharField(source="word_destination.name")
    language_source_name = serializers.CharField(source="language_source.name")
    language_destination_name = serializers.CharField(
        source="language_destination.name"
    )

    class Meta:
        model = Translation
        fields = "__all__"


class AddTranslationSerializerFromWord(serializers.ModelSerializer):
    word_source_name = serializers.CharField()
    word_destination_name = serializers.CharField()

    class Meta:
        model = Translation
        fields = (
            "language_source",
            "language_destination",
            "word_source_name",
            "word_destination_name",
        )


class FindWordv2_Serializer(serializers.ModelSerializer):
    id = serializers.CharField(source="word_source.id")
    name = serializers.CharField(source="word_source.name")
    language = serializers.CharField(source="language_source.name")

    class Meta:
        model = Translation
        fields = (
            "id",
            "name",
            "language",
        )
