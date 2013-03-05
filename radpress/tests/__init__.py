import os.path
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.test import TestCase
from django.test.client import Client
from radpress.models import Article
from radpress.templatetags.radpress_tags import restructuredtext


class Tests(TestCase):
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
