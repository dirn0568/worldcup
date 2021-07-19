from django.contrib import admin

# Register your models here.
from mainpage import forms


class SearchAdmin(admin.ModelAdmin):
    list_display = (u'preview', u'caption')
    search_fields = (u'caption')
    form = forms.PostDetailForm