from rest_framework import serializers
from blog.models import Post
from django.utils.text import slugify


class PostSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False)  
    autogenerate_slug = serializers.BooleanField(required=False
    ,write_only=True, default=False)
    
    class Meta:
        model = Post
        fields = "__all__"
        readonly = ["modified_at", "created_at"]

    def validate(self, data):
      if not data.get("slug"):
        if data["autogenerate_slug"]:
          data["slug"] = slugify(data["title"])
        else:
          raise serializers.ValidationError("slug is required if autogenerate_slug is not set")
      del data["autogenerate_slug"]
      return data

    