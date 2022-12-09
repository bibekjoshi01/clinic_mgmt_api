from . models import Blog
from rest_framework import serializers
from django.contrib.auth.models import User
from . models import * 

#blog serializers 

from django.contrib.auth import get_user_model
import os
from django.conf import settings

User = get_user_model()

class BlogCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

    def validate_title(self, value):
        if len(value) > 500:
            return serializers.ValidationError("Max title length is 500 characters")
        return value
    
    def clean_image(self, value):
        initial_path = value.path
        new_path = settings.MEDIA_ROOT + value.name
        os.rename(initial_path, new_path)
        return value



class BlogListSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField(read_only=True)

    class Meta: 
        model = Blog
        fields = '__all__'
    
    def get_comments(serf, obj):
        qs = Comment.objects.filter(parent=obj).count()
        return qs
    
    def get_url(self, obj):
        return obj.get_api_url()



class BlogDetailsSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    comments = serializers.SerializerMethodField(read_only=True)

    class Meta: 
        model = Blog
        fields = '__all__'
    
    def get_slug(self, obj):
        return obj.slug
    
    def get_comments(self, obj):
        qs = Comment.objects.filter(parent=obj)
        try: 
            serializer = CommentSerializer(qs, many=True)
        except Exception as e:
            print(e)
        return serializer.data

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CommentCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
    

