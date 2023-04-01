from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from user.models import User
from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        """ There you can create user """
        return super().post(request, *args, **kwargs)


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def get(self, request, *args, **kwargs):
        """ There you can get user """
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """ There you can update user """
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """ There you can зartial_update user """
        return super().patch(request, *args, **kwargs)
