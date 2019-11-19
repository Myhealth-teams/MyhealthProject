from django.shortcuts import render
from rest_framework import viewsets,mixins

from Myhealth_home.models import Rotations
from Myhealth_home.serializer import RotationsSerializer


class RotationsViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
    queryset = Rotations
    serializer_class = RotationsSerializer

