"""
WSGI config for website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")
#
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()

SITE_DIR = '/home/ec2-user/repo/my-website'
import site
site.addsitedir(SITE_DIR)

import os
import sys
sys.path.append(SITE_DIR)

os.environ['DJANGO_SETTINGS_MODULE'] = 'website.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()