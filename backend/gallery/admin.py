"""
Registering Gallery models with admin interface
"""

from django.contrib import admin

from backend.gallery.models import Image
admin.site.register(Image)
