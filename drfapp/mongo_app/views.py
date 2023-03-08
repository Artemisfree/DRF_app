from rest_framework.decorators import api_view
from rest_framework.response import Response
from pymongo import MongoClient
from .serializers import MappackSerializer


@api_view(['GET'])
def get_mappack(request):
    # Connect to MongoDB.
    client = MongoClient()
    db = client['mappacks']
    collection = db['mappack']
    # Get the parameters from request
    name = request.query_params.get('name')
    brand = request.query_params.get('brand')
    ecu = request.query_params.get('ecu')
    softwareversion = request.query_params.get('softwareversion')
    # Filter to find mappack
    filter = {
        'name': name,
        'brand': brand,
        'ecu': ecu,
        'softwareversion': softwareversion,
    }
    # Find needed mappack in db
    mappack = collection.find_one(filter)
    # Serialize mappack and return it
    serializer = MappackSerializer(mappack)
    if request.query_params.get('format') == 'csv':
        return Response(serializer.data.to_csv())
    elif request.query_params.get('format') == 'json':
        return Response(serializer.data)
    elif request.query_params.get('format') == 'a2l':
        return Response(serializer.data.to_a2l())
    elif request.query_params.get('format') == 'kp':
        return Response(serializer.data.to_kp())
    else:
        return Response(serializer.data)
