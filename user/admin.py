from django.contrib import admin
from django.forms import forms

from .forms import ContactForm
from .models import register, Feedback, Contact

# Register your models here.
admin.site.register(register)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'query')


admin.site.register(Feedback, FeedbackAdmin)

admin.site.register(Contact)
