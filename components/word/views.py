import random
from typing import OrderedDict

from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from components.translation.models import Translation
from components.translation.serializers import FindWordv2_Serializer
from components.word.models import Word
from components.word.serializers import WordSerializer

from components import language
from components.language.models import Language
from components.translation.models import Translation
from components.translation.serializers import (
    AddTranslationSerializerFromWord,
    GetTranslationSerializer,
)


@api_view(["GET", "POST", "OPTIONS"])
def word_list(request):
    """
    List all words, or create a new word
    """
    if request.method == "GET":
        language = Word.objects.all()
        serializer = WordSerializer(language, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        data["alpha_position"] = data["name"][0].lower()
        serializer = WordSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def find_word(
    request,
    pattern=None,
    language_src_id=None,
):
    """
    List all words, or create a new word
    """
    word = Word.objects.filter(name__contains=pattern, language__id=language_src_id)
    serializer = WordSerializer(word, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(["GET"])
def find_word_v2(request, pattern=None, language_src_id=None, language_dst_id=None):
    """
    List all words, or create a new word
    """
    word = Translation.objects.filter(
        word_source__name__contains=pattern,
        language_source__id=language_src_id,
        language_destination__id=language_dst_id,
    )
    serializer = FindWordv2_Serializer(word, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(["GET"])
def find_word_by_name(request, pattern=None, language_src=None, language_dst=None):
    """
    List all words, or create a new word
    """
    word = Translation.objects.filter(
        word_source__name__contains=pattern,
        language_source__name=language_src,
        language_destination__name=language_dst,
    )
    serializer = FindWordv2_Serializer(word, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(["GET", "PUT", "PATCH", "DELETE", "OPTIONS"])
def word_detail(request, pk):
    try:
        word = Word.objects.get(pk=pk)
    except Word.DoesNotExist:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = WordSerializer(word)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        serializer = WordSerializer(word, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "PATCH":
        serializer = WordSerializer(word, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({}, serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        word.delete()
        return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "OPTIONS"])
def mixed_word(request, language):
    """
    List all words, or create a new word
    """
    if request.method == "GET":
        word = Word.objects.filter(language__name=language)
        serializer = WordSerializer(word, many=True)
        _data = serializer.data
        result = list(filter(lambda x: _is_acceptable(x), _data))
        data = random.sample(result, 10)
        return JsonResponse(data, safe=False)


def _is_acceptable(_word):
    word = dict(_word).get("name")
    return word.isalnum() and len(word) <= 10




@api_view(["GET"])
def words_multi(request, pattern=None, language_src_id=None, language_dst_id=None):
    """
    List all words, or create a new word
    """

    # Search word pretraduction
    words_data = []
    for pat in pattern.rstrip("_").split("_"):
        word = Translation.objects.filter(
            word_source__name__contains=pat,
            language_source__id=language_src_id,
            language_destination__id=language_dst_id,
        )
        serializer = FindWordv2_Serializer(word, many=True)

        if serializer.data :
            words_data.append(serializer.data[0])


    # Get Translation
    translation_data = []
    for word in words_data :
        translation = Translation.objects.filter(
            word_source_id=word["id"],
            language_source_id=language_src_id,
            language_destination_id=language_dst_id,
        )
        serializer = GetTranslationSerializer(translation, many=True)

        if serializer.data :
            translation_data.append(serializer.data[0])


    return JsonResponse(translation_data, safe=False)


