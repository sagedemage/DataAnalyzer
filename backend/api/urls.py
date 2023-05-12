from django.urls import path

from . import views

urlpatterns = [
        path('register', views.register, name='register'),
        path('login', views.login, name='login'),
        path('add-table', views.add_table, name='add_table'),
        path('delete-table', views.delete_table, name='delete_table'),
        path('update-table', views.update_table, name='update_table'),
        path('view-tables', views.view_tables, name='view_tables'),
        path('add-row', views.add_row, name='add_row'),
        path('view-rows', views.view_rows, name='view_rows'),
        path('get-decoded-token', views.get_decoded_token, name='get-decoded-token'),
        path('test', views.test, name='test'),
]
