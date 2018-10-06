from django.contrib import admin
from myblog.models import Post, Category, Categorization


#  Model admin classes
class CategorizationInline(admin.TabularInline):
    model = Categorization
    extra = 1


class PostAdmin(admin.ModelAdmin):
    inlines = (CategorizationInline,)


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)


# admin registrations
#admin.site.register(CategorizationInline)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
