from django.shortcuts import render
from rest_framework import mixins, generics

# Create your views here.
class WeixinLoginAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    pass