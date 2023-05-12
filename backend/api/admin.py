from django.contrib import admin

# Register your models here.

from .models import User, Table, Row

admin.site.register(User)
admin.site.register(Table)
admin.site.register(Row)
