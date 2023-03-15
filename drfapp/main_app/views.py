import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework.parsers import FileUploadParser


@api_view(['POST'])
def get_options(request):
    file_data = request.data.get('file')
    # file_data = request.body  # Receive binary file from client
    server_url = 'http://example.com/server'  # Replace with the server URL
    files = {'file': file_data}
    # response = requests.post(server_url, data=file_data)  # Send file to server
    response = requests.post(server_url, files=files)
    options = response.content  # Get available options from server
    return Response(options, content_type='application/octet-stream')  # Return response to client in binary format


@api_view(['POST'])
def patch_file(request):
    file_data = request.data.get('file')
    # file_data = request.body
    server_url = 'http://example.com/server'
    files = {'file': file_data}
    # response = requests.post(server_url, data=file_data)
    response = requests.post(server_url, files=files)
    patched_file = response.content  # Get patched file from server
    return Response(patched_file, content_type='application/octet-stream')
