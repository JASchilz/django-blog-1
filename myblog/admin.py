from django.contrib import admin
from myblog.models import Post, Category


#  Model admin classes
class CategoryInline(admin.TabularInline):
    model = Category
    extra = 1


class PostAdmin(admin.ModelAdmin):
    inlines = (CategoryInline,)


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)


# admin registrations
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
