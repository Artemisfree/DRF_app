from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer


@api_view(['POST'])
def authenticate_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    dongle_serial = request.data.get('dongle_serial')
    user = User.objects.filter(
        username=username, password=password,
        dongle_serial=dongle_serial
        ).first()
    if user:
        serializer = UserSerializer(user)
        return Response(serializer.data)
    else:
        return Response(
            {'error': 'Invalid username, password, or dongle serial.'},
            status=status.HTTP_401_UNAUTHORIZED
            )
