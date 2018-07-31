from django.conf import settings

DEFAULT_NUMBER_BITS = getattr(settings, 'VERSION_FIELD_NUMBER_BITS', (8, 8, 16))
