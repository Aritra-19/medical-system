from django.contrib import admin
from django import forms
from api.models import User, Profile
from api.forms import ProfileForm

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']

class ProfileAdmin(admin.ModelAdmin):
    form = ProfileForm
    list_display = ['user', 'first_name', 'last_name', 'date_of_birth', 'phone_number', 'verified']
    list_editable = ['verified']

admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
