""" Table Operations """

from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from ..serializers import TableSerializer
from ..models import User, Table

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
            return HttpResponse("Add Table")
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


@csrf_exempt
@api_view(['GET'])
def fetch_table(request):
    """
    Route: /api/fetch-table
    URL Parameters:
    - table_id: integer
    """
    table_id = request.GET.get('id', '')
    table = Table.objects.get(id=table_id)
    name = table.name
    column1_name = table.column1_name
    column2_name = table.column2_name
    return JsonResponse({"name": name, "column1_name": column1_name, "column2_name": column2_name})
