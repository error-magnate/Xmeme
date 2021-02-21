from rest_framework import serializers
from xmeme.models import MemePost, HashTags

# Serializers for meme posts
class memePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemePost
        fields = "__all__"

# Serializers for tags
class hashTagsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = HashTags
        fields = "__all__"