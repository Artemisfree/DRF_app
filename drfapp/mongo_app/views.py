from rest_framework import generics
from rest_framework.response import Response
from .serializers import MappackSerializer
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
import pymongo


class MappackView(generics.RetrieveAPIView):
    serializer_class = MappackSerializer
    lookup_field = 'name'

    def retrieve(self, request, *args, **kwargs):
        # Get the mappack name from the request
        name = kwargs.get('name')
        # Connect to the MongoDB database
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = client['mappack']
        # Find the mappack file in the database
        mappack = db.mappacks.find_one({'name': name})
        if mappack is None:
            return Response(status=404)
        # Read the mappack file from the database
        file_data = mappack['file']
        # Decrypt the file data using RSA
        private_key = RSA.import_key(open('private_key.pem').read())
        cipher = PKCS1_OAEP.new(private_key)
        file_data = base64.b64decode(file_data)
        file_data = cipher.decrypt(file_data)
        # Return the decrypted file data
        return Response(file_data, content_type='application/octet-stream')
