import base64
import requests
import rsa

from django.http import JsonResponse, HttpResponse


def send_file(request):
    # Get the binary file from the client
    bin_file = request.FILES['bin_file'].read()

    # Encrypt the binary file using RSA encryption
    with open('public_key.pem', 'rb') as f:
        public_key = rsa.PublicKey.load_pkcs1(f.read())
    encrypted_data = rsa.encrypt(bin_file, public_key)

    # Encode the encrypted data as base64
    encrypted_data_b64 = base64.b64encode(encrypted_data).decode('utf-8')

    # Send the encrypted file to the server
    url = 'https://example.com/upload/'
    headers = {'Content-Type': 'application/json'}
    data = {'file_data': encrypted_data_b64}
    response = requests.post(url, headers=headers, json=data)

    # Return the server response to the client
    return JsonResponse({'server_response': response.json()})


def receive_file(request):
    # Receive the binary file from the server
    url = 'https://example.com/download/'
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)

    # Decode the encrypted file from base64
    encrypted_data_b64 = response.json()['file_data']
    encrypted_data = base64.b64decode(encrypted_data_b64)

    # Decrypt the encrypted file using RSA encryption
    with open('private_key.pem', 'rb') as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())
    decrypted_data = rsa.decrypt(encrypted_data, private_key)

    # Return the decrypted file to the client
    response = HttpResponse(content_type='application/octet-stream')
    response['Content-Disposition'] = 'attachment; filename="file.bin"'
    response.write(decrypted_data)
    return response
