"""
Registering Blog items with admin interface
"""

from django.contrib import admin

from backend.blog.models import Post
admin.site.register(Post)
