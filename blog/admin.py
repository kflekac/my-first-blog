from django.contrib import admin
#importing the Post class from the models file
from .models import Post


# Making the model visible on the admin page
admin.site.register(Post)
