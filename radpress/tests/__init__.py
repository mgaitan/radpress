import os.path
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.test import TestCase
from django.test.client import Client
from radpress.models import Article, Page, Tag
from radpress.templatetags.radpress_tags import restructuredtext


class Test(TestCase):
    fixtures = [os.path.join(os.path.dirname(__file__), 'data.json')]

    def setUp(self):
        self.client = Client()

        self.article1 = Article.objects.get(pk=1)

    def test_all_published_articles(self):
        # check published article count
        self.assertEqual(Article.objects.all_published().count(), 1)

        # check published page count
        self.assertEqual(Page.objects.all_published().count(), 2)

    def test_open_private_and_public_article_details(self):
        for article in Article.objects.all():
            status_code = 200 if article.is_published else 404
            response = self.client.get(
                reverse('radpress-detail', args=[article.slug]))

            self.assertEqual(response.status_code, status_code)

    def test_preview_page(self):


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
        tag_name = 'how I met your mother'
        tag = Tag.objects.create(name=tag_name)
        self.assertEqual(tag.slug, slugify(tag_name))

        # add tag to a published article and check count of tags
        self.article1.articletag_set.create(tag=tag)
        self.assertEqual(self.article1.tags.count(), 1)

        # try to filter articles for tags
        articles = Article.objects.filter(tags__name=tag_name)
        self.assertEqual(articles.count(), 1)
