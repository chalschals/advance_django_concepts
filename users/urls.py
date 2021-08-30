from django.urls import path
from .views import RegisterUserCreate, BlacklistTokenUpdateView

app_name = 'users'

urlpatterns = [
    path('register/', RegisterUserCreate.as_view(), name="create_user"),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist')
]
