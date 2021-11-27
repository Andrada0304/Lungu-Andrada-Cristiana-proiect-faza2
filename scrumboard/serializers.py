from rest_framework import serializers
from scrumboard.models import List,Card,User2

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

class ListSerilaizer(serializers.ModelSerializer):
    cards = CardSerializer(read_only=True, many=True)

    class Meta:
        model = List
        fields = '__all__'

class UserSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = User2
        fields = '__all__'