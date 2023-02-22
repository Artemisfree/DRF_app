from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CsvData
from .serializers import CsvDataSerializer
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# Generate public and private keys for RSA encryption
key = RSA.generate(2048)
public_key = key.publickey().export_key().decode('utf-8')
private_key = key.export_key().decode('utf-8')


@api_view(['POST'])
def receive_csv(request):
    # Decrypt CSV data using private key
    encrypted_csv_data = request.data['data']
    csv_data = decrypt_csv(encrypted_csv_data, private_key)

    # Save CSV data to database
    serializer = CsvDataSerializer(data={'data': csv_data})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def send_csv(request):
    # Get CSV data from database
    csv_data = CsvData.objects.all().first()
    if csv_data:
        serializer = CsvDataSerializer(csv_data)

        # Encrypt CSV data using public key
        encrypted_csv_data = encrypt_csv(serializer.data['data'], public_key)

        # Send encrypted CSV data to lua service
        response = requests.post('https://example.com',
                                 {'data': encrypted_csv_data})

        return Response(serializer.data)
    return Response(status=status.HTTP_404_NOT_FOUND)


def encrypt_csv(csv_data, public_key):
    cipher = PKCS1_OAEP.new(RSA.import_key(public_key))
    encrypted_csv_data = cipher.encrypt(csv_data.encode('utf-8'))
    return base64.b64encode(encrypted_csv_data).decode('utf-8')


def decrypt_csv(encrypted_csv_data, private_key):
    encrypted_csv_data = base64.b64decode(encrypted_csv_data.encode('utf-8'))
    cipher = PKCS1_OAEP.new(RSA.import_key(private_key))
    csv_data = cipher.decrypt(encrypted_csv_data).decode('utf-8')
    return csv_data
