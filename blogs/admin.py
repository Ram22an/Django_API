from django.contrib import admin
from .models import Blogs,Comments
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display=('blog_title',)

admin.site.register(Blogs,BlogAdmin)
admin.site.register(Comments)

