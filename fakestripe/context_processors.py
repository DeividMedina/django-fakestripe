from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static


def fakestripe_context_processor(request):
    """
    Context processor that provides 'stripejs_url' for use in templates.
    """
    if getattr(settings, 'FAKESTRIPE_ENABLED', False):
        stripejs_url = static('stripe.js')
    else:
        stripejs_url = 'https://js.stripe.com/v2/'
    return {
        'stripejs_url': stripejs_url,
    }
