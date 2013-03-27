from django import forms
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _
from radpress.models import Article, Entry, Page
from radpress.rst_extensions.rstify import parse_rst_data


class MarkupWidget(forms.Textarea):
    def render(self, name, value, attrs=None):
        html = super(MarkupWidget, self).render(name, value, attrs)
        html += """
            <script type="text/javascript">
                (function($) {
                    restSettings.previewParserPath = '%s';
                    $('textarea').markItUp(restSettings);
                })(django.jQuery);
            </script>
        """ % reverse('radpress-preview')

        return mark_safe(html)


class EntryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EntryForm, self).__init__(*args, **kwargs)

        # change content widget.
        content = self.fields.get('content')
        content.widget = MarkupWidget()


class ArticleForm(EntryForm):
    class Meta:
        model = Entry


class PageForm(EntryForm):
    class Meta:
        model = Page


class ZenModeForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)

    def clean_content(self):
        field = self.cleaned_data.get('content')
        self.data = parse_rst_data(field, metadata=True)

        if self.data.get('title') is None or self.data.get('slug') is None:
            msg = _("Title or slug can not be empty.")
            raise forms.ValidationError(msg)

        return field

    def save(self):
        article = Article.objects.create(**self.data)
        return article
