from components.translation.models import Translation
from typing import OrderedDict
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework import serializers, status
from rest_framework.parsers import JSONParser
from components.translation.models import Translation
from components.translation.serializers import TranslationSerializer


@api_view(['GET', 'POST', 'OPTIONS'])
def translation_list(request):
    """
    List all words, or create a new word
    """
    if request.method == 'GET':
        translation = Translation.objects.all()
        serializer = TranslationSerializer(translation, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TranslationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
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
    serializer = TranslationSerializer(translation, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'])
def translation_detail(request, pk):
    try:
        translation = Translation.objects.get(pk=pk)
    except Translation.DoesNotExist:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TranslationSerializer(translation)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = TranslationSerializer(translation, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = TranslationSerializer(translation,
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
    serializer = TranslationSerializer(translation, many=True)
    return JsonResponse(serializer.data, safe=False)
