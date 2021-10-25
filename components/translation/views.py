from components import language
from components.language.models import Language
from components.translation.models import Translation
from typing import OrderedDict
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework import serializers, status
from rest_framework.parsers import JSONParser
from components.translation.models import Translation
from components.translation.serializers import GetTranslationSerializer, AddTranslationSerializerFromWord
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from components.word.models import Word
from django.shortcuts import get_object_or_404


@api_view(['GET', 'OPTIONS'])
def translation_list(request):
    """
    List all words, or create a new word
    """
    translation = Translation.objects.all()
    serializer = GetTranslationSerializer(translation, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST', 'OPTIONS'])
@permission_classes((IsAuthenticated, ))
def create_translation(request):
    data = JSONParser().parse(request)
    serializer = AddTranslationSerializerFromWord(data=data)
    language_source = Language.objects.get(
        id=serializer.data['language_source'])
    language_destination = Language.objects.get(
        id=serializer.data['language_destination'])
    if serializer.is_valid():
        word_source = Word.objects.get_or_create(
            name=serializer.data['word_source_name'], language_id=serializer.data['language_source'])
        word_destination = Word.objects.get_or_create(
            name=serializer.data['word_destination_name'], language_id=serializer.data['language_destination'])
        result = Translation.objects.get_or_create(word_source=word_source[0],
                                                   language_source=language_source,
                                                   word_destination=word_destination[0],
                                                   language_destination=language_destination)
        res = Translation.objects.get(pk=result[0].pk)
        result_serializer = GetTranslationSerializer(res)
        return JsonResponse(result_serializer.data, status=status.HTTP_200_OK)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'OPTIONS'])
def find_translations(request, pattern=None, language_src_id=None, language_dst_id=None):
    """
    List all words, or create a new word
    """
    translation = Translation.objects.filter(
        word_source__name__contains=pattern,
        language_source_id=language_src_id,
        language_destination_id=language_dst_id)
    serializer = GetTranslationSerializer(translation, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'])
def translation_detail(request, pk):
    try:
        translation = Translation.objects.get(pk=pk)
    except Translation.DoesNotExist:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GetTranslationSerializer(translation)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = GetTranslationSerializer(translation, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = GetTranslationSerializer(translation,
                                              data=request.data,
                                              partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({}, serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        translation.delete()
        return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'OPTIONS'])
def get_translation(request, word_id=None, language_src_id=None, language_dst_id=None):
    """
    List all words, or create a new word
    """
    translation = Translation.objects.filter(
        word_source_id=word_id,
        language_source_id=language_src_id,
        language_destination_id=language_dst_id)
    serializer = GetTranslationSerializer(translation, many=True)
    return JsonResponse(serializer.data, safe=False)
