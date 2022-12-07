from rest_framework import serializers
from . models import *

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class Health_PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health_Package
        fields = '__all__'

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'

class AccreditationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accreditation
        fields = '__all__'

class Payment_MethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_Method
        fields = '__all__'

class FAQsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQs
        fields = '__all__'


class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, min_length=3, allow_blank=False)
    email = serializers.EmailField(allow_blank=False)
    phone = serializers.IntegerField()
    subject = serializers.CharField()
    message = serializers.CharField()


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
    

