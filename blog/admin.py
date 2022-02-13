from django.contrib import admin
from .models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _
from django_summernote.admin import SummernoteModelAdmin
from .models import User

# # Register your models here.

# admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Contact)

admin.site.register(Reply)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','comment', 'post', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('name', 'email', 'comment')

@admin.register(Post)
class CommentAdmin(SummernoteModelAdmin):
    list_display = ('id','title', 'post', 'created_date')
    list_filter = ('created_date',)
    summernote_fields = ('post',)



@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name','image')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


from django_summernote.utils import get_attachment_model
admin.site.unregister(get_attachment_model())