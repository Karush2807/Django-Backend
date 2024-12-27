#will take variables from models and convert them to string, then finally will be having json format of our model with data

from rest_framework import serializers
from .models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields=('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at')
