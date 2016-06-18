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
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.dev")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.prod")

application = get_wsgi_application()
