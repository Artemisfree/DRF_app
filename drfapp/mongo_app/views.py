import rsa
import base64
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Mappack
# from .serializers import MappackSerializer


class MappackView(APIView):
    def get(self, request, format=None):
        # Get the request parameters
        filename = request.query_params.get('filename', '')
        public_key = request.query_params.get('public_key', '')

        # Find the mappack in MongoDB
        mappack = Mappack.objects.filter(file__icontains=filename).first()

        # Encrypt the mappack with RSA
        with open('public_key.pem', 'wb') as f:
            f.write(public_key.encode())
        with open('public_key.pem', 'rb') as f:
            public_key = rsa.PublicKey.load_pkcs1(f.read())
        with open(mappack.file.path, 'rb') as f:
            data = f.read()
            encrypted_data = rsa.encrypt(data, public_key)
            encrypted_data_base64 = base64.b64encode(encrypted_data)

        # Return the encrypted mappack as a response
        return Response({
            'name': mappack.name,
            'file': encrypted_data_base64.decode(),
        })
