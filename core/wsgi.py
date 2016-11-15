"""
WSGI config for maddog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import ast

from django.core.wsgi import get_wsgi_application

debug = os.getenv("DEBUG", "False")

if ast.literal_eval(debug):
    settings_module = 'core.settings.dev'
else:
    settings_module = 'core.settings.prod'

os.environ['DJANGO_SETTINGS_MODULE'] = settings_module

application = get_wsgi_application()
