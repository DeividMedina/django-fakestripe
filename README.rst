==========
Fakestripe
==========

Fakestripe is a simple Django app to simulate the Stripe API. It's useful for
unit tests and working offline.

Quick start
-----------

1. Add "fakestripe" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'fakestripe',
    ]

2. Enable fakestripe like this::

    FAKESTRIPE_ENABLED = DEBUG

3. Include the fakestripe URLconf in your project ``urls.py`` like this::

    url(r'^fakestripe/', include('fakestripe.urls')),

4. In your template, reference the Stripe javascript library like this::

    <script type="text/javascript" src="{{ stripejs_url }}"></script>

5. Disable any backend stripe code that calls the Stripe API, e.g.::

    if not DEBUG:
        charge = stripe.Charge.create(
            customer=self.stripe_customer_id,
            amount=amount,
            currency='aud',
            description=description,
        )
        charge_id = charge.id
    else:
        charge_id = 'DUMMY_CHARGE_ID'

That's it!
