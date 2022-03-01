"""
Serializers for todoapp models
"""

from rest_framework import serializers
from .models import *


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'title',
        )
        model = Todo