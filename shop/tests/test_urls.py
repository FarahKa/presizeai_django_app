from django.test import SimpleTestCase
#use simple test case when you don't need to talk to the database
from django.urls import reverse, resolve
from shop.views import basic, createScan, getScan

class TestUrls(SimpleTestCase):
    def test_list_url_resolves(self):
        url = reverse("basic")
        self.assertEquals(resolve(url).func, basic)

    def test_create_scan_resolves(self):
        url = reverse("create_scan")
        self.assertEquals(resolve(url).func, createScan)

    def test_get_scan_resolves(self):
        url = reverse("get_scan")
        self.assertEquals(resolve(url).func, getScan)