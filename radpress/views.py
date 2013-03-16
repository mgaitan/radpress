from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.generic import (
    ArchiveIndexView, DetailView, FormView, ListView, TemplateView, UpdateView)
from radpress.mixins import ZenModeViewMixin, TagViewMixin, EntryViewMixin
from radpress.models import Article, Page
from radpress.settings import DATA


class IndexView(TagViewMixin, ListView):
    template_name = 'radpress/index.html'
    model = Article

    def get_queryset(self):
        return self.model.objects.all_published()[:DATA.get('RADPRESS_LIMIT')]

    def get_context_data(self, **kwargs):
        data = super(IndexView, self).get_context_data(**kwargs)
        data.update({'by_more': True})

        return data


class ArticleDetailView(TagViewMixin, EntryViewMixin, DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        data = super(ArticleDetailView, self).get_context_data(**kwargs)
        data.update({
            'object_list': self.model.objects.all_published().values(
                'slug', 'title', 'updated_at')[:DATA.get('RADPRESS_LIMIT')]
        })

        return data


class PageDetailView(TagViewMixin, EntryViewMixin, DetailView):
    model = Page


class ArchiveView(TagViewMixin, ArchiveIndexView):
    template_name = 'radpress/archive.html'
    model = Article
    date_field = 'created_at'
    paginate_by = 25

    def get_queryset(self):
        queryset = self.model.objects.all_published()

        # filter for tags, if possible...
        tag = self.request.GET.get('tag')
        if tag:
            queryset = queryset.filter(tags__slug=tag)

        return queryset.values('slug', 'title', 'updated_at')

    def get_context_data(self, **kwargs):
        data = super(ArchiveView, self).get_context_data(**kwargs)
        data.update({
            'enabled_tag': self.request.GET.get('tag')
        })

        return data


class PreviewView(TemplateView):
    template_name = 'radpress/preview.html'
    http_method_names = ['post']

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PreviewView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        data = super(PreviewView, self).get_context_data(**kwargs)
        data.update({
            'content': self.request.POST.get('data', '')
        })

        return data

    def post(self, request, *args, **kwargs):
        return super(PreviewView, self).get(request, *args, **kwargs)


class SearchView(TemplateView):
    template_name = 'radpress/search.html'
    models = (Article, Page)

    def get_queryset(self):
        queryset = []
        q = self.request.GET.get('q')

        if not q:
            return queryset

        for model in self.models:
            queryset += model.objects.filter(
                Q(title__icontains=q) | Q(slug__icontains=q) |
                Q(content__icontains=q), is_published=True)

        return queryset

    def get_context_data(self, **kwargs):
        data = super(SearchView, self).get_context_data(**kwargs)
        data.update({'object_list': self.get_queryset()})

        return data


class ZenModeView(ZenModeViewMixin, FormView):
    pass


class ZenModeUpdateView(ZenModeViewMixin, UpdateView):
    pass
