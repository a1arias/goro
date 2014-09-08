from django.test import TestCase
from django.core.urlresolvers import reverse

class ArticalIndexViewTests(TestCase):
    def test_index_view_with_no_articles(self):
        """
        If no articles exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('articles:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Articles")
        self.assertQuerysetEqual(response.context['articles'], [])
