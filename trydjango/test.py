from django.test import TestCase
import os
from django.conf import settings
from django.contrib.auth.password_validation import validate_password


class TryDjango(TestCase):
    def test_secret_key(self):
        SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

        try:
            is_strong = validate_password(SECRET_KEY)
        except Exception as e:
            msg = f'Week Scret key {e.messages}'
            self.fail(msg)