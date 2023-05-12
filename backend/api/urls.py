from django.urls import path

from . import views

urlpatterns = [
        path('register', views.register, name='register'),
        path('login', views.login, name='login'),
        path('add-table', views.add_table, name='add_post'),
        path('view-tables', views.view_tables, name='view_posts'),
        path('get-decoded-token', views.get_decoded_token, name='get-decoded-token'),
        path('test', views.test, name='test'),
]
