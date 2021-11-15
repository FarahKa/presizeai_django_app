from django.test import TestCase, Client
from django.urls import reverse
from shop.models import Scan
import json
from datetime import date, timedelta

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.basic_url = reverse("basic")
        self.get_scan_url = reverse("get_scan")
        self.scan1 = Scan.objects.create(
            sizeid="abc", last_activity=date.today()
        )
        self.scan2 = Scan.objects.create(
            sizeid="abcd", last_activity=date.today() - timedelta(61)
        )

    def test_basic_get(self):
        response = self.client.get(self.basic_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "shopfront.html")

    def test_get_scan_succeeded(self):
        response = self.client.post(self.get_scan_url, {"sizeid_input" : "abc"})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "shopfront.html")

    def test_get_scan_too_old(self):
        response = self.client.post(self.get_scan_url, {"sizeid_input" : "abcd"})
        self.assertEquals(response.status_code, 401)
        self.assertTemplateUsed(response, "shopfront.html")

    def test_get_scan_not_found(self):
        response = self.client.post(self.get_scan_url, {})
        self.assertEquals(response.status_code, 404)
        self.assertTemplateUsed(response, "shopfront.html")