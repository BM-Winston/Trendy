from django.contrib import admin

from .models import Profile, User, Business, N_Hood

# Register your models here.
admin.site.register(Profile)
admin.site.register(User)
admin.site.register(Business)
admin.site.register(N_Hood)
