from django.contrib import admin
from .models import work
from .models import restore
from .models import buy

# Register your models here.

admin.site.register(work)
admin.site.register(restore)
admin.site.register(buy)
