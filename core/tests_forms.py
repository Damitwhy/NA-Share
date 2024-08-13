from django.test import TestCase
from .forms import CommentForm, ShareForm, ContactForm, SearchForm, SignInForm

class TestForms(TestCase):

    def test_comment_form_valid_data(self):
        form = CommentForm(data={
            'content': 'This is a test comment'
        })
        self.assertTrue(form.is_valid())

    def test_comment_form_no_data(self):
        form = CommentForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def test_share_form_valid_data(self):
        form = ShareForm(data={
            'title': 'Test Share',
            'content': 'This is a test share content'
        })
        self.assertTrue(form.is_valid())

    def test_share_form_no_data(self):
        form = ShareForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)

    def test_contact_form_valid_data(self):
        form = ContactForm(data={
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'This is a test message'
        })
        self.assertTrue(form.is_valid())

    def test_contact_form_no_data(self):
        form = ContactForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)

    def test_search_form_valid_data(self):
        form = SearchForm(data={
            'query': 'Test search'
        })
        self.assertTrue(form.is_valid())

    def test_search_form_no_data(self):
        form = SearchForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def test_signin_form_valid_data(self):
        form = SignInForm(data={
            'username': 'test',
            'password': 'sameagain123'
        })
        self.assertTrue(form.is_valid())

    def test_signin_form_no_data(self):
        form = SignInForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)