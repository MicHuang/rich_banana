from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.
class UserManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(phone='123456', password='foo')
        self.assertEqual(user.phone, '123456')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_admin)
        self.assertFalse(user.is_staff)
        # username does not exist for AbstractBaseUser
        with self.assertRaises(AttributeError):
            user.username
        # TypeError with nothing
        with self.assertRaises(TypeError):
            User.objects.create_user()
        # TypeError without password
        with self.assertRaises(TypeError):
            User.objects.create_user(phone='')
        # ValueError with blank phone Number
        with self.assertRaises(ValueError):
            User.objects.create_user(phone='', password='foo')

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(phone='123456', password='foo')
        self.assertEqual(admin_user.phone, '123456')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_admin)
        self.assertTrue(admin_user.is_staff)
        # username does not exist for AbstractBaseUser
        with self.assertRaises(AttributeError):
            admin_user.username
        with self.assertRaises(ValueError):
            User.objects.create_superuser(phone='123456', password='foo', is_superuser=False)
