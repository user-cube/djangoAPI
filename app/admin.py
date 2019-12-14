from django.contrib import admin

# Register your models here.
from app.models import Items, Profile, Encomenda

admin.site.register(Items)
admin.site.register(Profile)
admin.site.register(Encomenda)
