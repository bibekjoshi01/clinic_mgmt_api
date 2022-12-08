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
    '''
        This is Accreditation API
    '''

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



#-----------------------------------------------------------

# blog views
from django.shortcuts import redirect, get_object_or_404
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,
)
class CreatePostAPIView(APIView):
  
    queryset = Blog.objects.all()
    serializer_class = BlogCreateUpdateSerializer


    def post(self, request, *args, **kwargs):
        serializer = BlogCreateUpdateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            return Response(serializer.data, status=200)
        else:
            return Response({"errors": serializer.errors}, status=400)


class ListBlogAPIView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogListSerializer


class DetailBlogAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    lookup_field = "slug"
    serializer_class = BlogDetailsSerializer


class CreateCommentAPIView(APIView):

    serializer_class = CommentCreateUpdateSerializer

    def blog(self, request, slug, *args, **kwargs):
        blog = get_object_or_404(Post, slug=slug)
        serializer = CommentCreateUpdateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user, parent=blog)
            return Response(serializer.data, status=200)
        else:
            return Response({"errors": serializer.errors}, status=400)


class ListCommentAPIView(APIView):
    """
    get:
        Returns the list of comments on a particular post
    """

    def get(self, request, slug):
        blog = Blog.objects.get(slug=slug)
        comments = Comment.objects.filter(parent=blog)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=200)


class DetailCommentAPIView(RetrieveUpdateDestroyAPIView):
    """
    get:
        Returns the details of a comment instance. Searches comment using comment id and post slug in the url.
    put:
        Updates an existing comment. Returns updated comment data
        parameters: [parent, author, body]
    delete:
        Delete an existing comment
        parameters: [parent, author, body]
    """

    #permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    queryset = Comment.objects.all()
    lookup_fields = ["parent", "id"]
    serializer_class = CommentCreateUpdateSerializer