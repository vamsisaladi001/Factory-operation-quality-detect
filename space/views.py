from django.shortcuts import render
from rest_framework import generics
from .serializers import SuperSerializer
from .models import Super
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView
from .models import QualityInspection
from .serializers import QualityInspectionSerializer

# Create your views here.
class listall(ListAPIView):
    queryset=Super.objects.all()
    serializer_class=SuperSerializer
class postall(CreateAPIView):
    queryset=Super.objects.all()
    serializer_class=SuperSerializer
class delete(DestroyAPIView):
    queryset=Super.objects.all()
    serializer_class=SuperSerializer
class update(UpdateAPIView):
    queryset=Super.objects.all()
    serializer_class=SuperSerializer
class QualityInspectionListCreateView(generics.ListCreateAPIView):
    queryset = QualityInspection.objects.select_related("work_order").all()
    serializer_class = QualityInspectionSerializer


class QualityInspectionDetailView(generics.RetrieveAPIView):
    queryset = QualityInspection.objects.select_related("work_order").all()
    serializer_class = QualityInspectionSerializer