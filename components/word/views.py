from typing import OrderedDict
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework import serializers, status
from rest_framework.parsers import JSONParser
from components.word.models import Word
from components.language.models import Language
from components.word.serializers import WordSerializer
from components.language.serializers import LanguageSerializer


@api_view(['GET', 'POST', 'OPTIONS'])
def word_list(request):
    """
    List all words, or create a new word
    """
    if request.method == 'GET':
        language = Word.objects.all()
        serializer = WordSerializer(language, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        data["alpha_position"] = data["name"][0].lower()
        serializer = WordSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'])
def word_detail(request, pk):
    try:
        word = Word.objects.get(pk=pk)
    except Word.DoesNotExist:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WordSerializer(word)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = WordSerializer(word, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = WordSerializer(word,
                                    data=request.data,
                                    partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({}, serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        word.delete()
        return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
