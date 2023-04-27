from rest_framework import serializers
from .models import Tourist


class TouristSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tourist
        fields = ('title', 'cat_id')