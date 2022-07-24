from django.contrib import admin
from .models import About
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _
from django_summernote.admin import SummernoteModelAdmin
from blog.models import User


# Register your models here.
@admin.register(About)
class CommentAdmin(SummernoteModelAdmin):
    list_display = ('id', 'name', 'email', 'phone')
    summernote_fields = ('description',)


@admin.register(User)
class ModelOptions(admin.ModelAdmin):
    fieldsets = (
        ('', {
            'fields': ('email', "first_name", "last_name", "image"),
        }),
        ('Flags', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ("is_active",), }),
    )
