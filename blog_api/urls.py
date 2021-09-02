from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostList  # PostLister, PostDetail
app_name = 'blog_api'

# These following 2 urls wont work for viewsets, we need router to handel viewsets
# urlpatterns = [
#     # path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
#     # path('', PostLister.as_view(), name='listcreate'),
# ]


routers = DefaultRouter()
routers.register('', PostList, basename='user')
urlpatterns = routers.urls
