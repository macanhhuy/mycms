# -*- coding: utf-8 -*-
from django.contrib import admin
from blog.models import Post, Category, Comment, Image
from tinymce.widgets import TinyMCE
from django.core.urlresolvers import reverse

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 3
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)
    
class ImageInline(admin.StackedInline):
    model = Image
    sortable_field_name = "position"
    fields = ("image", "position",)
    extra = 3
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)  
     
class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline, ImageInline]
    list_filter = ('title',) 
    search_fields = ('title', 'content')
    filter_horizontal = ('category',)
    raw_id_fields = ('user',) 
    
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'content', 'category')
        }),
        ('Advanced options', {
            'classes': ('grp-collapse grp-open',),
            'fields': ('thumbnail', 'user', 'tags')
        }),
    )
#    def formfield_for_dbfield(self, db_field, **kwargs):
#        if db_field.name in ('content'):
#            return db_field.formfield(widget=TinyMCE(
#                attrs={'cols': 100, 'rows': 30},
#                mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')},
#            ))  
#        return super(PostAdmin, self).formfield_for_dbfield(db_field, **kwargs)
    class Media:
        js = ['/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js', 
                '/static/grappelli/tinymce_setup/tinymce_setup.js',]
class CategoryAdmin(admin.ModelAdmin):
    fields = ('title' , 'position',)
    sortable_field_name = 'position'
    search_fields = ('title',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
