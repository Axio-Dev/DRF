import json
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse

from products.models import Product


def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        # this is a serialization and do the following things:
        # 1-. model instance (model_data)
        # 2-. turn a Python dict
        # 3-. Return JSON to my client
        data = model_to_dict(model_data, fields=["id", "title", "price"])
    return JsonResponse(data)
    #     print(data)
    #     data = dict(data)
    #     json_data_str = json.dumps(data)
    # return JsonResponse(json_data_str, headers={"content_type": "application/json"})