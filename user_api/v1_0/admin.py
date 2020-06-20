from django.contrib import admin
from v1_0.models import (
    Log, 
    Person, Group, Department
)

# Register your models here.

admin.site.register(Log)
admin.site.register(Person)

admin.site.register(Group)
admin.site.register(Department)

