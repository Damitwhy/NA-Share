from django.test import TestCase
from django.utils import timezone
from core.models import User, Profile, VisitorCount, Share, Comment, Message, Rating, ServiceLink, ContactMessage

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345', is_admin=True)

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertTrue(self.user.is_admin)

class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile.objects.create(user=self.user, name='Test Profile', bio='This is a test bio.')

    def test_profile_creation(self):
        self.assertEqual(self.profile.user.username, 'testuser')
        self.assertEqual(self.profile.name, 'Test Profile')
        self.assertEqual(self.profile.bio, 'This is a test bio.')

class VisitorCountModelTest(TestCase):
    def setUp(self):
        self.visitor_count = VisitorCount.objects.create(count=10)

    def test_visitor_count_creation(self):
        self.assertEqual(self.visitor_count.count, 10)

class ShareModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.share = Share.objects.create(user=self.user, title='Test Share', content='This is a test share.')

    def test_share_creation(self):
        self.assertEqual(self.share.user.username, 'testuser')
        self.assertEqual(self.share.title, 'Test Share')
        self.assertEqual(self.share.content, 'This is a test share.')
        self.assertEqual(self.share.status, 'pending')
        self.assertEqual(self.share.average_rating, 0)

class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.share = Share.objects.create(user=self.user, title='Test Share', content='This is a test share.')
        self.comment = Comment.objects.create(share=self.share, user=self.user, content='This is a test comment.')

    def test_comment_creation(self):
        self.assertEqual(self.comment.share.title, 'Test Share')
        self.assertEqual(self.comment.user.username, 'testuser')
        self.assertEqual(self.comment.content, 'This is a test comment.')
        self.assertFalse(self.comment.approved)

class MessageModelTest(TestCase):
    def setUp(self):
        self.sender = User.objects.create_user(username='sender', password='12345')
        self.receiver = User.objects.create_user(username='receiver', password='12345')
        self.message = Message.objects.create(sender=self.sender, receiver=self.receiver, content='This is a test message.')

    def test_message_creation(self):
        self.assertEqual(self.message.sender.username, 'sender')
        self.assertEqual(self.message.receiver.username, 'receiver')
        self.assertEqual(self.message.content, 'This is a test message.')
        self.assertFalse(self.message.is_read)

class RatingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.share = Share.objects.create(user=self.user, title='Test Share', content='This is a test share.')
        self.rating = Rating.objects.create(share=self.share, user=self.user, rating_value=5)

    def test_rating_creation(self):
        self.assertEqual(self.rating.share.title, 'Test Share')
        self.assertEqual(self.rating.user.username, 'testuser')
        self.assertEqual(self.rating.rating_value, 5)

class ServiceLinkModelTest(TestCase):
    def setUp(self):
        self.service_link = ServiceLink.objects.create(url='http://example.com', description='This is a test service link.')

    def test_service_link_creation(self):
        self.assertEqual(self.service_link.url, 'http://example.com')
        self.assertEqual(self.service_link.description, 'This is a test service link.')

class ContactMessageModelTest(TestCase):
    def setUp(self):
        self.contact_message = ContactMessage.objects.create(name='Test User', email='test@example.com', message='This is a test message.')

    def test_contact_message_creation(self):
        self.assertEqual(self.contact_message.name, 'Test User')
        self.assertEqual(self.contact_message.email, 'test@example.com')
        self.assertEqual(self.contact_message.message, 'This is a test message.')