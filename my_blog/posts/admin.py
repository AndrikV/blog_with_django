from django.contrib import admin

from .models import Posts, PostsComments

admin.site.register(Posts)
admin.site.register(PostsComments)
