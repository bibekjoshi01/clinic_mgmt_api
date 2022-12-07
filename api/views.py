from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework import viewsets

class ServiceModelViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    
class DoctorModelViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DepartmentModelViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class Health_PackageModelViewSet(viewsets.ModelViewSet):
    queryset = Health_Package.objects.all()
    serializer_class = Health_PackageSerializer

class TestModelViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class TestimonialModelViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class AccreditationModelViewSet(viewsets.ModelViewSet):
    queryset = Accreditation.objects.all()
    serializer_class = AccreditationSerializer

class FAQsModelViewSet(viewsets.ModelViewSet):
    queryset = FAQs.objects.all()
    serializer_class = FAQsSerializer



#class based views 

# class ServiceAPI(APIView):
#     def get(self, request, pk=None, format=None):
#         if pk is not None:
#             service = Service.objects.get(id=pk)
#             serializer = ServiceSerializer(service)
#             return Response(serializer.data)
#         else:
#             service = Service.objects.all()
#             serializer = ServiceSerializer(service, many=True)
#             return Response(serializer.data)
    
#     def post(self, request, format=None):
#         serializer = ServiceSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg":'Service Created Successfully'}, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk=None, format=None):
#         service = Service.objects.get(id=pk)
#         serializer = ServiceSerializer(service, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Service Updated Successfully'})
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request, pk=None, format=None):
#         service = Service.objects.get(id=pk)
#         serializer = ServiceSerializer(service, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Service Updated Successfully'})
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk=None, format=None):
#         service = Service.objects.get(id=pk)
#         service.delete()
#         return Response({'msg':'Service Deleted Successfully'}
from django.core.mail import send_mail

class ContactView(APIView):
    serializer_class = ContactSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = ContactSerializer(data = request.data)
        if serializer_class.is_valid():
            data = serializer_class.validated_data
            name = data.get('name')
            email = data.get('email')
            message = data.get('message')

            send_mail('Contact Form Mail from ' + name, message, email, ['bibekjoshi34@gmail.com'],)

            return Response({"success":"sent"}, status=status.HTTP_200_OK)
        else:
            return Response({"error":"failed"}, status=status.HTTP_400_BAD_REQUEST)

