from django.contrib import admin
from my_app.models import Person, Car, Rent
from django.contrib.auth.admin import UserAdmin
from .forms import SignUpForm
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = Person
    add_form = SignUpForm
    fieldsets = (
        *UserAdmin.fieldsets,
        (
        'User role',
        {
            'fields':(
            'person_id',
            'phone_number',
            'city',
            'age'
            )
        }
        )
    )
   


admin.site.register(Person, CustomUserAdmin)
admin.site.register(Car)
admin.site.register(Rent)