from django.urls import path
from rest_framework.routers import DefaultRouter
# PostLister, PostDetail
from .views import (PostList, PostDetail, PostCustomSearch,
                    PostSearch, CreatePost, EditPost, DeletePost, AdminPostDetails as apd)
app_name = 'blog_api'

# These following 2 urls wont work for viewsets, we need router to handel viewsets
urlpatterns = [

    path('search/custom', PostCustomSearch.as_view(), name='postsearch'),
    # /search/custom?slug=me-and-you

    path('search/', PostSearch.as_view(), name='detailfilter'),
    # /search/?search=keyword_to_search ##RECOMMAND ONE

    path('admin/create/', CreatePost.as_view(), name='createpost'),
    path('admin/details/<int:pk>/', apd.as_view(), name='adminpostdetails'),
    path('admin/edit/<int:pk>/', EditPost.as_view(), name='editpost'),
    path('admin/delete/<int:pk>/', DeletePost.as_view(), name='deletepost'),

    path('<str:pk>/', PostDetail.as_view(), name='detailcreate'),
    path('', PostList.as_view(), name='listcreate'),


]


# routers = DefaultRouter()
# routers.register('', PostList, basename='user')
# urlpatterns = routers.urls
