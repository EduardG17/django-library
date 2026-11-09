from django.contrib import admin
from .models import Edition, Reader, Copy, Issue

admin.site.register(Edition)
admin.site.register(Reader)
admin.site.register(Copy)
admin.site.register(Issue)