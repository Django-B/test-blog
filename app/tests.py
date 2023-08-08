from django.test import TestCase
from .models import User

from dataclasses import dataclass

@dataclass
class TestUser:
    name: str
    email: str
    password: str
    updated_email: str

testuser = TestUser(
    name='testuser',
    email='testuser@mail.ru',
    password='testuser_password',
    updated_email='updated_testuser@mail.ru'
)

class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create( # type: ignore
            name=testuser.name,
            email=testuser.email,
            password=testuser.password
        )
    def test_user_fields(self):
        self.assertEqual(self.user.name, testuser.name)
        self.assertEqual(self.user.email, testuser.email)
        self.assertTrue(self.user.check_pass(testuser.password))

    def test_user_creation(self):
        user = User.objects.get(name=testuser.name) # type: ignore
        self.assertEqual(user.email, testuser.email)
        self.assertTrue(user.check_pass(testuser.password))

    def test_user_update(self):
        self.user.email = testuser.updated_email
        self.user.save()
        updated_user = User.objects.get(name=testuser.name) # type: ignore
        self.assertEqual(updated_user.email, testuser.updated_email)

