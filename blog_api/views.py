from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from blog.models import Post, Category
from .serializers import PostSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
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


class PostList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    #queryset = Post.objects.all()

    # optioanal

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)

    # custom queryset.. get_queryset function or queryset property either one required
    def get_queryset(self):
        return Post.objects.all()


# class PostList(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = Post.postobjects.all()

#     def list(self, request):
#         serializer_class = PostSerializer(self.queryset, many=True)
#         return Response(serializer_class.data)

#     def retrieve(self, request, pk=None):
#         post = get_object_or_404(self.queryset, pk=pk)
#         serializer_class = PostSerializer(post)
#         return Response(serializer_class.data)


# class PostLister(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = Post.postobjects.all()
#     serializer_class = PostSerializer
# class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermision):
#     # PostUserWritePermision==>GET for everyone /PUT & DELETE ONLY FOR POST CREATOR
#     permission_classes = [PostUserWritePermision]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
'''
@@@@@ViewSet Functions@@@@@
# def list(self, request):
#     pass

# def create(self, request):
#     pass

# def retrieve(self, request, pk=None):
#     pass

# def update(self, request, pk=None):
#     pass

# def partial_update(self, request, pk=None):
#     pass

# def destroy(self, request, pk=None):
#     pass
'''

# *****************************************************************

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
