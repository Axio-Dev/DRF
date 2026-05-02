import json
from django.http import JsonResponse

from products.models import Product


def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price
        # this is a serialization and do the following things:
        # 1-. model instance (model_data)
        # 2-. turn a Python dict
        # 3-. Return JSON to my client
    return JsonResponse(data)