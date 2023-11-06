from django.urls import path
from .views import CreatePostView, LikePostView, UnlikePostView, AnalyticsView, UserActivityView, \
    UserRegistrationAPIView, UserLoginAPIView, UserRetrieveUpdateAPIView

urlpatterns = [
    path('api/user/', UserRetrieveUpdateAPIView.as_view(), name='retrieve_user'),
    path('api/register/', UserRegistrationAPIView.as_view(), name='register_user'),
    path('api/login/', UserLoginAPIView.as_view(), name='login_user'),
    path('api/create_post/', CreatePostView.as_view(), name='create_post'),
    path('api/like_post/<int:pk>/', LikePostView.as_view(), name='like_post'),
    path('api/unlike_post/<int:pk>/', UnlikePostView.as_view(), name='unlike_post'),
    path('api/analytics/', AnalyticsView.as_view(), name='analytics'),
    path('api/user_activity/<int:pk>/', UserActivityView.as_view(), name='user_activity'),
]
