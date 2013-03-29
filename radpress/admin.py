from django.contrib import admin
from radpress.models import Article, EntryImage, Menu, Page, Tag
from radpress.forms import PageForm, ZenModeForm


class MarkupAdminMixin(object):
    class Media:
        css = {
            'all': ('radpress/css/editor.css',)
        }
        js = (
            'radpress/markitup/jquery.markitup.js',
            'radpress/markitup/set.js')


class EntryAdmin(admin.ModelAdmin, MarkupAdminMixin):
    list_display = ['title', 'created_at', 'updated_at', 'is_published']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('is_published',)
    search_fields = ('title',)


class ArticleAdmin(admin.ModelAdmin):
    form = ZenModeForm
    list_display = (
        'title', 'author', 'created_at', 'updated_at', 'tag_list',
        'is_published')
    list_filter = ('is_published', 'tags')
    list_editable = ('is_published',)

    def tag_list(self, obj):
        tag_list = [tag.name for tag in obj.tags.all()]

        return ', '.join(tag_list)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user

        obj.save()

admin.site.register(Article, ArticleAdmin)


class PageAdmin(EntryAdmin):
    form = PageForm

admin.site.register(Page, PageAdmin)


class TagAdmin(admin.ModelAdmin):
    def articles(self, obj):
        return obj.article_set.count()

    list_display = ['name', 'slug', 'articles']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Tag, TagAdmin)
admin.site.register(Menu, admin.ModelAdmin)


class EntryImageAdmin(admin.ModelAdmin):
    list_display = ('thumbnail_tag', '__unicode__', 'name')
    list_display_links = ('__unicode__',)
    search_fields = ('image', 'name')

admin.site.register(EntryImage, EntryImageAdmin)
