from rest_framework.response import Response
from api import models, serializers
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
    ListCreateAPIView,
    DestroyAPIView,
)


# Create your views here.


class StudentListView(ListAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer


class StudentDetailsView(RetrieveAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer


class StudentCreate(ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer


class StudentUpdate(RetrieveUpdateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer


class StudentDelete(DestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
