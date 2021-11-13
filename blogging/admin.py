from django.contrib import admin
from blogging.models import Post, Category

# Register your models here.


class CategoryInline(admin.TabularInline):
    model = Category


class PostAdmin(admin.ModelAdmin):
    pass
    inlines = [
        CategoryInline,
    ]


class CategoryAdmin(admin.ModelAdmin):
    exclude = ["posts"]


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
