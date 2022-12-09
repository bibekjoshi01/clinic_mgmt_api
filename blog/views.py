from django.shortcuts import render
from . serializers import *
from . models import *
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


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
class CreatePostAPIView(CreateAPIView):
  
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