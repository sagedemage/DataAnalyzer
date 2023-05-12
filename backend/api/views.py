from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt;
from rest_framework.decorators import api_view
from .serializers import UserSerializer, TableSerializer, RowSerializer
from .models import User, Table
from django.contrib.auth.hashers import make_password, check_password

from dotenv import load_dotenv
import jwt
import os
# Create your views here.

load_dotenv()  # take environment variables from .env.

""" Authentication """

@csrf_exempt
@api_view(['POST'])
def register(request):
    """
    Route: /api/register
    Request Parameters:
    - email: string
    - username: string
    - password: string
    """
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        email_match = User.objects.filter(email__exact=serializer.data.get("email"))
        username_match = User.objects.filter(username__exact=serializer.data.get("username"))
        password = serializer.data.get("password")
        if email_match.exists() is True:
            return JsonResponse({'registered': False, 'err_msg': "Email Already exists"})
        elif username_match.exists() is True:
            return JsonResponse({'registered': False, 'err_msg': "Username Already exists"})
        else:
            hashed_password = make_password(password)
            user = User(email=serializer.data.get("email"), username=serializer.data.get("username"),
                        password=hashed_password)
            user.save()
            return JsonResponse({'registered': True, 'success_msg': "User Registration Success"})


@csrf_exempt
@api_view(['POST'])
def login(request):
    """
    Route: /api/login
    Request Parameters:
    - username: string
    - password: string
    """
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        email_match = User.objects.filter(email__exact=serializer.data.get("username"))
        username_match = User.objects.filter(username__exact=serializer.data.get("username"))
        entered_password = serializer.data.get("password")
        if email_match.exists():
            actual_password = email_match.values_list('password', flat=True).get()
            password_match = check_password(entered_password, actual_password)
            if password_match:
                user_id = email_match.values_list('id', flat=True).get()
                token = generate_token(user_id)
                return JsonResponse({'auth': True, 'token': token, 'success_msg': "Successful Login"})
            else:
                return JsonResponse({'auth': False, 'err_msg': "Failed to Login"})
        elif username_match.exists():
            actual_password = username_match.values_list('password', flat=True).get()
            password_match = check_password(entered_password, actual_password)
            if password_match:
                user_id = username_match.values_list('id', flat=True).get()
                token = generate_token(user_id)
                return JsonResponse({'auth': True, 'token': token, 'success_msg': "Successful Login"})
            else:
                return JsonResponse({'auth': False, 'err_msg': "Failed to Login"})
        else:
            return JsonResponse({'auth': False, 'err_msg': "User does not exist"})
    else:
        return JsonResponse({'auth': False, 'err_msg': "Data is not valid"})


""" Table Operations """

@csrf_exempt
@api_view(['POST'])
def add_table(request):
    """
    Route: /api/add-table
    Request Parameters:
    - user_id: integer
    - name: string
    - column1_name: string
    - column1_name: string
    """
    serializer = TableSerializer(data=request.data)
    if serializer.is_valid():
        user_id = request.data.get("user_id")
        print("user id: " + str(user_id))
        user = User.objects.filter(id=user_id)
        if user.exists():
            table = Table(
                    name=serializer.data.get("name"),
                    column1_name=serializer.data.get("column1_name"),
                    column2_name=request.data.get("column2_name"),
                    user_id=user_id
            )
            table.save()
            return HttpResponse("Added Table")
        else:
            return HttpResponse("User Does Not Exist")
    else:
        return HttpResponse("Data not valid")


@csrf_exempt
@api_view(['DELETE'])
def delete_table(request):
    """
    Route: /api/delete-table
    Request Parameters:
    - user_id: integer
    - table_id: integer
    """
    user_id = request.data.get("user_id")
    table_id = request.data.get("table_id")
    user = User.objects.filter(id=user_id)
    if user.exists():
        table = Table.objects.filter(id=table_id)
        table.delete()
        return HttpResponse("Delete Table")
    else:
        return HttpResponse("User Does Not Exist")


@csrf_exempt
@api_view(['PATCH'])
def update_table(request):
    """
    Route: /api/update-table
    Request Parameters:
    - user_id: integer
    - table_id: integer
    - name: string
    - column1_name: string
    - column1_name: string
    """
    serializer = TableSerializer(data=request.data)
    if serializer.is_valid():
        user_id = request.data.get("user_id")
        table_id = request.data.get("table_id")
        user = User.objects.filter(id=user_id)
        if user.exists():
            table = Table.objects.get(id=table_id)
            if table != "":
                table.name = serializer.data.get("name")
                table.column1_name = serializer.data.get("column1_name")
                table.column2_name = serializer.data.get("column2_name")
                table.save()
                return HttpResponse("Update Table")
        else:
            return HttpResponse("User Does Not Exist")
    else:
        return HttpResponse("Data not valid")


@csrf_exempt
@api_view(['POST'])
def view_tables(request):
    """
    Route: /api/view-tables
    Request Parameters:
    - user_id: integer
    """
    user_id = request.data.get("user_id")
    tables = Table.objects.filter(user_id__exact=user_id)
    serializer = TableSerializer(tables, many=True)
    return JsonResponse({'tables': serializer.data})


""" Row Operations """

@csrf_exempt
@api_view(['POST'])
def add_row(request):
    """
    Request Parameters:
    - table_id: integer
    - name: string
    - column1_data: string
    - column1_data: string
    """
    serializer = RowSerializer(data=request.data)
    if serializer.is_valid():
        user = User.objects.filter(id=request.data.get("table_id"))
        if user.exists():
            table = Table(
                    name=serializer.data.get("name"),
                    column1_name=serializer.data.get("column1_data"),
                    column2_name=request.data.get("column2_data")
            )
            table.save()
            return HttpResponse("Added Row")
        else:
            return HttpResponse("Table Does Not Exist")
    else:
        return HttpResponse("Data not valid")


@csrf_exempt
@api_view(['POST'])
def view_rows(request):
    table_id = request.data.get("table_id")
    tables = Table.objects.filter(table_id__exact=table_id)
    serializer = TableSerializer(tables, many=True)
    return JsonResponse({'rows': serializer.data})


""" JWT Operations """

@csrf_exempt
@api_view(['POST'])
def get_decoded_token(request):
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


@csrf_exempt
@api_view(['GET', 'POST'])
def test(request):
    if request.method == 'GET':
        return JsonResponse({'test': 'test1'})
    elif request.method == 'POST':
        test_data = request.data.get("test")
        return JsonResponse({'test': test_data})
