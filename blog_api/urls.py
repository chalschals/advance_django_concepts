from django.urls import path
from .views import PostLister, PostDetail
app_name = 'blog_api'


urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    path('', PostLister.as_view(), name='listcreate'),
]
