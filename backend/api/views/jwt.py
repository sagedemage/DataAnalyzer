""" JWT Operations """

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt;
from rest_framework.decorators import api_view

from dotenv import load_dotenv
import jwt
import os
# Create your views here.

load_dotenv()  # take environment variables from .env.


@csrf_exempt
@api_view(['POST'])
def get_decoded_token(request):
    """
       Request Parameters:
       - token: string
    """
    token = request.data.get("token")
    decoded_token = decode_token(token)
    auth = decoded_token.get('auth')
    user_id = decoded_token.get('user_id')
    return JsonResponse({'auth': auth, 'user_id': user_id})


def generate_token(user_id):
    secret = os.getenv("JWT_SECRET")
    encoded = jwt.encode({"auth": True, "user_id": user_id}, secret, algorithm="HS256")
    return encoded


def decode_token(encoded):
    secret = os.getenv("JWT_SECRET")
    decoded = jwt.decode(encoded, secret, algorithms=["HS256"])
    return decoded
