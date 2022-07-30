from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.parsers import JSONParser
from components.language.models import Language
from components.language.serializers import LanguageSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


@api_view(["GET", "OPTIONS"])
def language_list(request):
    """
    List all transformers, or create a new language
    """
    language = Language.objects.all()
    serializer = LanguageSerializer(language, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(["POST", "OPTIONS"])
@permission_classes((IsAuthenticated,))
def add_language(request):
    data = JSONParser().parse(request)
    serializer = LanguageSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET','PUT','PATCH','DELETE', 'OPTIONS'])
# def language_detail(request, pk):
#     try:
#         language = Language.objects.get(pk=pk)
#     except Language.DoesNotExist:
#         return JsonResponse(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = LanguageSerializer(language)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         serializer = LanguageSerializer(language, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors,
#                         status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'PATCH':
#         serializer = LanguageSerializer(language,
#                                            data=request.data,
#                                            partial=True)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse({},serializer.errors,
#                         status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         language.delete()
#         return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
