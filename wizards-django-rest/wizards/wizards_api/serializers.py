from rest_framework import serializers
from .models import Wizard, House, Founder
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','email']


class WizardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wizard
        fields = ['id', 'name', 'house']


class HouseSerializer(serializers.ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(many=True, queryset=Wizard.objects.all())

    class Meta:
        model = House
        fields = ['id', 'name','founder']


class FounderSerializer(serializers.ModelSerializer):
    houses = serializers.PrimaryKeyRelatedField(many=True, queryset=House.objects.all())

    class Meta:
        model = Founder
        fields = ['id', 'name']