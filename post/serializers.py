from dataclasses import field
from pyexpat import model
from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"