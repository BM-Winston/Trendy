from django.contrib import admin

from .models import Profile, Business, N_Hood, Post

# Register your models here.
admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(N_Hood)
admin.site.register(Post)
