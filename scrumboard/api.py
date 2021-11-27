from rest_framework.viewsets import ModelViewSet
from scrumboard.serializers import  ListSerilaizer, CardSerializer ,UserSerilaizer
from django.contrib import admin
from scrumboard.models import List, Card, User2
class ListViewSet(ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerilaizer


class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class RegisterView(ModelViewSet):
    queryset = User2.objects.all()
    serializer_class = UserSerilaizer