from django.urls import path

from . import views
from .views import row, table, auth, test, jwt

urlpatterns = [
        # authentication
        path('register', auth.register, name='register'),
        path('login', auth.login, name='login'),

        # jwt
        path('get-decoded-token', jwt.get_decoded_token, name='get-decoded-token'),

        # table
        path('add-table', table.add_table, name='add_table'),
        path('delete-table', table.delete_table, name='delete_table'),
        path('update-table', table.update_table, name='update_table'),
        path('view-tables', table.view_tables, name='view_tables'),
        path('fetch-table', table.fetch_table, name='fetch_table'),

        # row
        path('add-row', row.add_row, name='add_row'),
        path('update-row', row.update_row, name='update_row'),
        path('delete-row', row.delete_row, name='delete_row'),
        path('view-rows', row.view_rows, name='view_rows'),
        path('fetch-row', row.fetch_row, name='fetch_row'),

        # test
        path('test', test.test, name='test'),
]
