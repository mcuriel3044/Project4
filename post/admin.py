from django.contrib import admin

#import post model
from .models import Post
# Register your models here.
admin.site.register(Post)
