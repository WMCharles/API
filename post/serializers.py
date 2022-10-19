from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):

    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'image', 'image_url')

    def get_image_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.image.url)