from django.http import Http404
from rest_framework import status, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Wizard, House, Founder
from .serializers import WizardSerializer, HouseSerializer, UserSerializer, FounderSerializer


class UserList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class WizardList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        wizards = Wizard.objects.all()
        serializer = WizardSerializer(wizards, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WizardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WizardDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_wizard(self, pk):
        try:
            return Wizard.objects.get(pk=pk)
        except Wizard.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        wizard = self.get_wizard(pk)
        serializer = WizardSerializer(wizard)
        return Response(serializer.data)

    def put(self, request, pk):
        wizard = self.get_wizard(pk)
        serializer = WizardSerializer(wizard, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        wizard = self.get_wizard(pk)
        wizard.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class HouseList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        houses = House.objects.all()
        serializer = HouseSerializer(houses, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HouseDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class FounderList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_founder(self, pk):
        try:
            return Founder.objects.get(pk=pk)
        except Founder.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        founder = self.get_founder(pk)
        serializer = FounderSerializer(founder)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        founder = self.get_founder(pk)
        serializer = FounderSerializer(founder, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        founder = self.get_founder(pk)
        founder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FounderDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_founder(self, pk):
        try:
            return Founder.objects.get(pk=pk)
        except Founder.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        founder = self.get_founder(pk)
        serializer = FounderSerializer(founder)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        founder = self.get_founder(pk)
        serializer = FounderSerializer(founder, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        founder = self.get_founder(pk)
        founder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)