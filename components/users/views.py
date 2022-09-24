from django.shortcuts import render

import random
from typing import OrderedDict

from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from django.contrib.auth import get_user_model
from django.test import TestCase

from components.users.models import UsersManagers


@api_view(["POST"])
def create_user(request):
    """
    
    """
    if "email" in request.data and "password" in request.data :
        usersManager = UsersManagers()
        user_created = usersManager.create_user(request.data["email"], request.data["password"])
        
        if user_created:
            return JsonResponse({"user":request.data["email"], "valid":True}, status=status.HTTP_200_OK)

    return JsonResponse({"user":request.data["email"], "valid":False}, status=status.HTTP_400_BAD_REQUEST)










