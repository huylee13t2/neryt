from django.contrib import admin
from app.models import Category, Tag, Post, Static_Page, Demo


class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'count', 'updated', 'created']


class TagAdmin(admin.ModelAdmin):
	list_display = ['name', 'count', 'updated', 'created']


class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'default_thumb', 'views', 'provider', 'link', 'updated', 'created']


# class Post_CategoryAdmin(admin.ModelAdmin):
# 	list_display = ['post', 'category']


# class Post_TagAdmin(admin.ModelAdmin):
# 	list_display = ['post', 'tag']


class Static_PageAdmin(admin.ModelAdmin):
	list_display = ['name_page', 'title']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
# admin.site.register(Post_Category, Post_CategoryAdmin)
# admin.site.register(Post_Tag, Post_TagAdmin)
admin.site.register(Static_Page, Static_PageAdmin)

# admin.site.register(Demo)
