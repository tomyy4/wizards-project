from rest_framework import serializers
from .models import Wizard, House


class WizardSerializer(serializers.Serializer):
    def create(self, validated_data):
        """
        Create and return a new `Wizard` instance, given the validated data.
        """
        return Wizard.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Wizard` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.code = validated_data.get('house', instance.house)
        instance.save()
        return instance


class HouseSerializer(serializers.Serializer):
    def create(self, validated_data):
        """
        Create and return a new `House` instance
        """
        return House.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `House` instance
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance