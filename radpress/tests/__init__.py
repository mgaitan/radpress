import os.path
from django.template.defaultfilters import slugify
from django.test import TestCase
from django.test.client import Client
from radpress.models import Article, Tag
from radpress.templatetags.radpress_tags import restructuredtext


class Test(TestCase):
    fixtures = [os.path.join(os.path.dirname(__file__), 'data.json')]

    def setUp(self):
        self.client = Client()

    def test_all_published_articles(self):
        self.assertEqual(Article.objects.all_published().count(), 1)

    def test_slugs(self):
        for article in Article.objects.all():
            slug = slugify(article.slug)
            self.assertEqual(article.slug, slug)

    def test_contents(self):
        for article in Article.objects.all():
            content_body = restructuredtext(article.content)
            self.assertEqual(article.content_body, content_body)

    def test_tags(self):
        # checks tag count from fixture
        self.assertEqual(Tag.objects.count(), 2)

        # create new tag and check slug
        tag = Tag.objects.create(name='how I met your mother')
        self.assertEqual(tag.slug, 'how-i-met-your-mother')