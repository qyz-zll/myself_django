"""
ASGI config for debuga project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'debuga.settings')

application = get_asgi_application()
