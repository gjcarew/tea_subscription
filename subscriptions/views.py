
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from subscriptions.models import Customer
from subscriptions.serializers import CustomerSerializer
