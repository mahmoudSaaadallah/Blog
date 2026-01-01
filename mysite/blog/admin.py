from django.contrib import admin
from .models import Post
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug':('title', )} # This attribute will make the slug field filled in automatically, using the title field.
    raw_id_fields = ['author'] # This will display a lookup widget which can be much better than an input drop-list when we have thousands of users.
    # As we could use the id for the user and look for him then select him using only the id.
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    show_facets = admin.ShowFacets.ALWAYS

