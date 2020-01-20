from django.contrib import admin
from .models import Product, Comment
# Register your models here.

class BookInline(admin.StackedInline):
    model = Comment

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', )
    search_fields = ['name']
    inlines = [
        BookInline
    ]
    

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_at',)
    search_fields = ['author']


admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentAdmin)
