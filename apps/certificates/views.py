# from django.shortcuts import render
from rest_framework import serializers, viewsets
# from django.contrib.auth import get_user_model
from .models import Certificate
# Create your views here.


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ('id','name','description', 'created_at','updated_at')


class CertificateViewSet(viewsets.ModelViewSet):
    # queryset = User.objects.all()
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer