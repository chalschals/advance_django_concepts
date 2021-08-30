from django.shortcuts import render
from rest_framework import generics
from blog.models import Post, Category
from .serializers import PostSerializer
from rest_framework.permissions import (
    SAFE_METHODS, IsAdminUser, IsAuthenticatedOrReadOnly, IsAuthenticated,
    DjangoModelPermissionsOrAnonReadOnly, DjangoModelPermissions, BasePermission)
# Create your views here.


class PostUserWritePermision(BasePermission):
    message = "You Dont Have Access To Edit This Post"

    def has_object_permission(self, request, view, obj):
        # print(request.method, SAFE_METHODS)
        # print(obj.auther, request.user)
        if request.method in SAFE_METHODS:
            return True
        return obj.auther == request.user


class PostLister(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermision):
    # PostUserWritePermision==>GET for everyone /PUT & DELETE ONLY FOR POST CREATOR
    permission_classes = [PostUserWritePermision]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


'''
@@@@@Concrete View Classes@@@@@
#CreateAPIView
Used for create-only endpoints.
#ListAPIView
Used for read-only endpoints to represent a collection of model instances.
#RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
#DestroyAPIView
Used for delete-only endpoints for a single model instance.
#UpdateAPIView
Used for update-only endpoints for a single model instance.
##ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
#RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
#RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
'''
