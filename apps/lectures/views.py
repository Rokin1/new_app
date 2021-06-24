# from django.shortcuts import render
from rest_framework import serializers, viewsets
# from django.contrib.auth import get_user_model
from .models import Lecture
# Create your views here.


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ('id', 'title', 'description', 'lecturer_name','date',
                  'duration', 'slides_url', 'is_required')


class LectureViewSet(viewsets.ModelViewSet):
    # queryset = User.objects.all()
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer