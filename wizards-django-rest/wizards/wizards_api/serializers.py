from rest_framework import serializers
from .models import Wizard, House


class WizardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wizard
        fields = ['id', 'name', 'house']


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ['id', 'name']