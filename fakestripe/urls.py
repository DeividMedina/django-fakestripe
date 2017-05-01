from django.conf.urls import url
import fakestripe.views

urlpatterns = [
      url(r'^$', fakestripe.views.api_base, name='fakestripe:api_base'),
      url(r'^v1/customers$', fakestripe.views.customers),
      url(r'^v1/charges$', fakestripe.views.charges),
]
