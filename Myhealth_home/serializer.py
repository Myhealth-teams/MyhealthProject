from rest_framework import serializers

from Myhealth_home.models import *


class RotationsSerializer(serializers.ModelSerializer):

    model = Rotations
    fields = "__all__"


