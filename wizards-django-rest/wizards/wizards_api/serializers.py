from rest_framework import serializers
from .models import Wizard, House, Founder, Subject, Spell
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','email']


class FounderSerializer(serializers.ModelSerializer):
    houses = serializers.StringRelatedField(many=True)

    class Meta:
        model = Founder
        fields = ['id', 'name']


class HouseSerializer(serializers.ModelSerializer):
    students = serializers.StringRelatedField(many=True)

    class Meta:
        model = House
        fields = ['id', 'name','students']


class WizardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wizard
        fields = ['id', 'name','house']


class SubjectSerializer(serializers.ModelSerializer):
    spells = serializers.StringRelatedField(many=True)

    class Meta:
        model = Subject
        fields = ['id', 'subject_name', 'spells']


class SpellSerializer(serializers.ModelSerializer):

    class Meta:
        model = Spell
        fields = ['id', 'spell_name','learnt_in']
