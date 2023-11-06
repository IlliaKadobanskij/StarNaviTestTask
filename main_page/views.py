from rest_framework import generics, status
from django.db.models import Count
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Post, UserActivity
from .permissions import CustomIsAuthenticated
from .serializers import PostSerializer, UserSerializer, AnalyticsSerializer, RegistrationSerializer, LoginSerializer, \
    UserActivitySerializer
from rest_framework.views import APIView


class UserRegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserLoginAPIView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (CustomIsAuthenticated,)
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})

        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class CreatePostView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (CustomIsAuthenticated,)

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class LikePostView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (CustomIsAuthenticated,)

    def perform_update(self, serializer):
        serializer.instance.likes.add(self.request.user)


class UnlikePostView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (CustomIsAuthenticated,)

    def perform_update(self, serializer):
        serializer.instance.likes.remove(self.request.user)


class AnalyticsView(generics.ListAPIView):
    serializer_class = AnalyticsSerializer

    def get_queryset(self):
        date_from = self.request.GET.get('date_from')
        date_to = self.request.GET.get('date_to')

        if date_from and date_to:
            return (
                Post.objects.filter(created_at__date__range=[date_from, date_to])
                    .values('created_at__date')
                    .annotate(likes_count=Count('likes'))
            )
        else:
            return []


class UserActivityView(generics.RetrieveAPIView):
    queryset = UserActivity.objects.all()
    serializer_class = UserActivitySerializer
