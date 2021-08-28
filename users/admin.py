from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, BillingAddress

from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',
                    'first_name', 'last_name']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('Address', 'City',
                           'Date_Of_Birth', 'Gender', 'Occupation', 'objective', 'Age', 'Country', 'PostalCode', 'AboutMe')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(BillingAddress)