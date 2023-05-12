""" Row Operations """

from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt;
from rest_framework.decorators import api_view
from ..serializers import RowSerializer
from ..models import User, Table, Row


@csrf_exempt
@api_view(['POST'])
def add_row(request):
    """
    Request Parameters:
    - user_id: integer
    - table_id: integer
    - column1_data: string
    - column1_data: string
    """
    serializer = RowSerializer(data=request.data)
    if serializer.is_valid():
        user_id = request.data.get("user_id")
        table_id = request.data.get("table_id")
        user = User.objects.filter(id=user_id)
        table = Table.objects.filter(id=table_id)
        if user.exists():
            if table.exists():
                row = Row(
                    column1_data=request.data.get("column1_data"),
                    column2_data=request.data.get("column2_data"),
                    table_id=table_id,
                )
                row.save()
                return HttpResponse("Add Row")
            else:
                return HttpResponse("Table Does Not Exist")
    else:
        return HttpResponse("Data not valid")


@csrf_exempt
@api_view(['PATCH'])
def update_row(request):
    """
    Request Parameters:
    - user_id: integer
    - table_id: integer
    - row_id: integer
    - column1_data: string
    - column1_data: string
    """
    serializer = RowSerializer(data=request.data)
    if serializer.is_valid():
        user_id = request.data.get("user_id")
        table_id = request.data.get("table_id")
        row_id = request.data.get("row_id")
        user = User.objects.filter(id=user_id)
        table = Table.objects.filter(id=table_id)
        if user.exists():
            if table.exists():
                row = Row.objects.get(id=row_id)
                row.column1_data = request.data.get("column1_data")
                row.column2_data = request.data.get("column2_data")
                row.save()
                return HttpResponse("Update Row")
            else:
                return HttpResponse("Table Does Not Exist")
    else:
        return HttpResponse("Data not valid")


@csrf_exempt
@api_view(['DELETE'])
def delete_row(request):
    """
    Request Parameters:
    - user_id: integer
    - table_id: integer
    - row_id: integer
    """
    user_id = request.data.get("user_id")
    table_id = request.data.get("table_id")
    row_id = request.data.get("row_id")
    user = User.objects.filter(id=user_id)
    table = Table.objects.filter(id=table_id)
    if user.exists():
        if table.exists():
            row = Row.objects.filter(id=row_id)
            row.delete()
            return HttpResponse("Delete Row")
        else:
            return HttpResponse("Table Does Not Exist")


@csrf_exempt
@api_view(['POST'])
def view_rows(request):
    """
    Request Parameters:
    - user_id: integer
    - table_id: integer
    """
    user_id = request.data.get("user_id")
    table_id = request.data.get("table_id")
    user = User.objects.filter(id=user_id)
    table = Table.objects.filter(id=table_id)
    if user.exists():
        if table.exists():
            rows = Row.objects.filter(table_id__exact=table_id)
            serializer = RowSerializer(rows, many=True)
            return JsonResponse({'rows': serializer.data})