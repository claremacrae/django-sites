from django.conf.app_template import admin
from django.contrib import admin
from .models import Post

admin.site.register(Post)

