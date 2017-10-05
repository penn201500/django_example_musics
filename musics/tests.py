# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import resolve

from django.test import TestCase
from views import hello_view
from views import display_musics
# Create your tests here.

class HelloViewTest(TestCase):

    def test_hello_url_resolve_to_hello_view(self):
        found = resolve('/hello/')
        self.assertEqual(found.func, hello_view)


class MusicsViewTest(TestCase):

    def test_musics_url_resolve_to_musics_view(self):
        found = resolve('/musics/')
        self.assertEqual(found.func, display_musics)
