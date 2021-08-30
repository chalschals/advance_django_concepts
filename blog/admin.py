from django.contrib import admin
from django.db import models
from . import models
# Register your models here.


@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status', 'slug', 'auther')
    prepopulated_fields = {'slug': ('title',), }


# admin.site.register(Post)
admin.site.register(models.Category)
