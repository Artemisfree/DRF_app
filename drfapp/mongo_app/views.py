from rest_framework import generics
from rest_framework.response import Response
from .models import Mappack
from .serializers import MappackSerializer
import os


class MappackView(generics.RetrieveAPIView):
    serializer_class = MappackSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            mappack = Mappack.objects.get(**kwargs)
            file_path = mappack.file.path
            file_format = os.path.splitext(file_path)[1][1:]
            with open(file_path, 'rb') as f:
                if file_format == 'csv':
                    response = Response(f, content_type='text/csv')
                elif file_format == 'json':
                    response = Response(f, content_type='application/json')
                elif file_format == 'a2l':
                    response = Response(
                        f,
                        content_type='application/octet-stream'
                    )
                elif file_format == 'kp':
                    response = Response(
                        f,
                        content_type='application/octet-stream'
                    )
                else:
                    response = Response(status=400)
            return response
        except Mappack.DoesNotExist:
            return Response(status=400)
