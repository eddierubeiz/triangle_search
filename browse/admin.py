from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import TriangleIssue, TriangleArticle

admin.site.register(TriangleIssue)
admin.site.register(TriangleArticle)
