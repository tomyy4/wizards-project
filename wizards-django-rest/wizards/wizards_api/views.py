from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Wizard, House
from .serializers import WizardSerializer, HouseSerializer


@api_view(['GET','POST'])
def wizards_list(request):
    if request.method == 'GET':
        wizards = Wizard.objects.all()
        serializer = WizardSerializer(wizards, many=True)
        return Response(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = WizardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def wizard_detail(request, pk):
    try:
        wizard = Wizard.objects.get(pk=pk)
    except Wizard.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WizardSerializer(wizard)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WizardSerializer(wizard, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        wizard.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def house_list(request):
    if request.method == 'GET':
        houses = House.objects.all()
        serializer = HouseSerializer(houses, many=True)
        return Response(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = HouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def house_detail(request, pk):
    try:
        house = House.objects.get(pk=pk)
    except House.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HouseSerializer(house)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WizardSerializer(house, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        house.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
