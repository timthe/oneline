from django.contrib import admin
from line.models import Category, Item, Comment


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_editable = ['name']
    search_fields = ['name']
    ordering = ['name']


class ItemAdmin(admin.ModelAdmin):
    # Add 할 때 나오는 form 종류
    fields = ['category', 'title', 'text']
    # Add 된 내용들 display 할 때 나타나는 내용들
    list_display = ['id', 'category', 'title', 'user', 'created']
    # list display 시 오른쪽 옆에 있는 filter 에 들어갈 것
    list_filter = ['category', 'user']
    # list display 시 바로 edit 할 수 있는 것
    list_editable = ['category']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'text']
    ordering = ['-created']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'created', 'item', 'user']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Comment, CommentAdmin)