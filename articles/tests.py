from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.utils.text import slugify
from articles.models import Article, Reporter

def create_article(headline, reporter):
    now = timezone.now()
    Article.objects.create(pub_date=now,
                           headline=headline, reporter=reporter)

def create_reporter(n):
    Reporter.objects.create(full_name=n)

class ArticalIndexViewTests(TestCase):
    def test_index_view_with_no_articles(self):
        """
        If no articles exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('articles:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Articles")
        self.assertQuerysetEqual(response.context['articles'], [])


class ArticleDetailViewTests(TestCase):
    def test_detail_view_with_valid_slug(self):
        create_reporter("Adrian")
        reporter = Reporter.objects.get(full_name="Adrian")
        create_article("test post 1", reporter)
        slug = slugify("test post 1")
        response = self.client.get(reverse('articles:detail',
                                           args=(slug,)))

        self.assertEqual(response.status_code, 200)
