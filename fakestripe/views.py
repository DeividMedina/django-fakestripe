from django.http import Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt


def api_base(request):
    # This view is just a placeholder so that the URL can be referred to by name.
    raise Http404()


@csrf_exempt
def charges(request):
    return JsonResponse({
        'id': 'fake-charge-id',
    })


@csrf_exempt
def customers(request):
    return JsonResponse({
        'id': request.POST['source'][0],
        'sources': {
            'total_count': 1,
            'data': [
                {
                    'brand': 'Visa',
                    'exp_month': 12,
                    'exp_year': 2020,
                    'last4': '1234',
                    'name': 'Mr Foobar',
                },
            ],
        },
    })
