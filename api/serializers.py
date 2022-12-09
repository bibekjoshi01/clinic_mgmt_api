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


