from django.conf import settings

from radpress.tests.base import BaseTest

if 'django.contrib.admin' in settings.INSTALLED_APPS:
    print("`django.contrib.admin` is not installed, passed admin tests...")
    from radpress.tests.admin import AdminTest
