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



from django.contrib.admin.widgets import AdminFileWidget

class AdminImageWidget(AdminFileWidget):

    def render(self, name, value, attrs=None, renderer=None):
        output = []

        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)

            output.append(
                f' <a href="{image_url}" target="_blank">'
                f'  <img src="{image_url}" alt="{file_name}" width="150" height="150" '
                f'style="object-fit: cover;"/> </a>')

        output.append(super(AdminFileWidget, self).render(name, value, attrs, renderer))
        return mark_safe(u''.join(output))

class GalleryAdminInline(admin.StackedInline):
    model = Gallery
    list_display = ("id",)
    extra = 1

    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget}
    }


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('id','title', 'post',"thumbnail_preview", 'created_date')
    list_filter = ('created_date',)
    summernote_fields = ('post',)
    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.image_preview

    thumbnail_preview.short_description = 'Image Preview'
    thumbnail_preview.allow_tags = True
    inlines = [GalleryAdminInline]



@admin.register(User)
class ModelOptions(admin.ModelAdmin):
    fieldsets = (
        ('', {
        'fields': ('email',"first_name","last_name"),
        }),
        ('Flags', {
        'classes': ('grp-collapse grp-closed',),
        'fields' : ("is_active",),}),
        ('Tags', {
            'classes': ('grp-collapse grp-open',),
            'fields' : ('password',),
            }),
)

from django_summernote.utils import get_attachment_model
admin.site.unregister(get_attachment_model())