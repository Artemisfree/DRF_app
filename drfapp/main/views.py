from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.forms import HexFileForm
import requests


def upload_hex_file(request):
    if request.method == 'POST':
        form = HexFileForm(request.POST, request.FILES)
        if form.is_valid():
            hex_file = request.FILES['hex_file']
            url = 'https://example.com/drf_app'  # need URL
            headers = {'Content-Type': 'application/octet-stream'}
            response = requests.post(url, headers=headers,
                                     data=hex_file.read())
            return redirect('receive_hex_file',
                            hex_file=response.content.decode())
    else:
        form = HexFileForm()
    return render(request, 'app_name/upload_hex_file.html', {'form': form})


def receive_hex_file(request, hex_file):
    return render(request,
                  'main/receive_hex_file.html',
                  {'hex_file': hex_file})
