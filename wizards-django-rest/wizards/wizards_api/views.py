from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .models import Wizard, House, Founder, Subject, Spell
from .serializers import WizardSerializer, HouseSerializer, UserSerializer, FounderSerializer, SubjectSerializer, \
    SpellSerializer


class UserList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class WizardList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Wizard.objects.all()
    serializer_class = WizardSerializer


class WizardDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Wizard.objects.all()
    serializer_class = WizardSerializer


class HouseList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class HouseDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class FounderList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Founder.objects.all()
    serializer_class = FounderSerializer


class FounderDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Founder.objects.all()
    serializer_class = FounderSerializer


class SubjectList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SpellList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Spell.objects.all()
    serializer_class = SpellSerializer


class SpellDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Spell.objects.all()
    serializer_class = SpellSerializer
