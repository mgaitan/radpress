from django import VERSION as DJANGO_VERSION
try:
    from django.utils.encoding import force_text
except ImportError:
    from django.utils.encoding import force_unicode as force_text

if DJANGO_VERSION >= (1, 5):
    # Django 1.5+ compatibility
    from django.contrib.auth import get_user_model
    User = get_user_model()  # NOQA

else:
    from django.contrib.auth.models import User  # NOQA
