from django.test import TestCase, Client
from django.urls import reverse
from .models import Share, Comment, ContactMessage, User  # Import your custom User model

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test', password='sameagain123', email='test@testtest.com')
        self.share = Share.objects.create(title='Test Share', user=self.user)
        self.comment = Comment.objects.create(content='Test Comment', share=self.share, user=self.user)
        self.share_list_url = reverse('home')
        self.create_share_url = reverse('create_share')
        self.edit_share_url = reverse('edit_share', args=[self.share.id])
        self.delete_share_url = reverse('delete_share', args=[self.share.id])
        self.contact_url = reverse('contact')

    def test_share_list_view(self):
        response = self.client.get(self.share_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/home.html')

    def test_create_share_view_GET(self):
        self.client.login(username='test', password='sameagain123')
        response = self.client.get(self.create_share_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/create_share.html')

    def test_create_share_view_POST(self):
        self.client.login(username='test', password='sameagain123')
        response = self.client.post(self.create_share_url, {
            'title': 'New Share',
            'description': 'This is a new share.'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Share.objects.last().title, 'New Share')

    def test_edit_share_view_GET(self):
        self.client.login(username='test', password='sameagain123')
        response = self.client.get(self.edit_share_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/edit_share.html')

    def test_edit_share_view_POST(self):
        self.client.login(username='test', password='sameagain123')
        response = self.client.post(self.edit_share_url, {
            'title': 'Updated Share',
            'description': 'This is an updated share.'
        })
        self.assertEqual(response.status_code, 200)
        self.share.refresh_from_db()
        self.assertEqual(self.share.title, 'Updated Share')

    def test_delete_share_view_GET(self):
        self.client.login(username='test', password='sameagain123')
        response = self.client.get(self.delete_share_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/delete_share.html')

    def test_delete_share_view_POST(self):
        self.client.login(username='test', password='sameagain123')
        response = self.client.post(self.delete_share_url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Share.objects.filter(id=self.share.id).exists())

    def test_contact_view_GET(self):
        response = self.client.get(self.contact_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/contact.html')

    def test_contact_view_POST(self):
        response = self.client.post(self.contact_url, {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'This is a test message.'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ContactMessage.objects.last().name, 'Test User')