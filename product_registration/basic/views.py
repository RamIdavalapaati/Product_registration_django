import json
from datetime import datetime
from urllib.parse import parse_qs, urlparse

from django.shortcuts import render
from django.core import serializers
from django.forms.models import model_to_dict
from django.http import HttpResponse, StreamingHttpResponse, JsonResponse

from basic.models import Product

DATE_FORMAT = "%Y-%m-%d"

def _convert_date_to_str(product):
    d = product["date_of_manufacture"]
    product["date_of_manufacture"] = d.strftime(DATE_FORMAT)
    return product

def _convert_str_to_date(product):
    d = product["date_of_manufacture"]
    product["date_of_manufacture"] = datetime.strptime(d, "%Y-%m-%d").date()
    return product

def _parse_args(path):
    urlp = urlparse(path)
    query_string = urlp.query
    param_vals = dict((k, v[0]) for k, v in parse_qs(query_string).items())
    return param_vals

def serialize_data(data):
    return json.dumps(data) + "\n"

def register_product(request):
    # TODO: Handle kwargs that comes in the body
    kwargs = _parse_args(request.get_full_path())
    kwargs = _convert_str_to_date(kwargs)

    product = Product(**kwargs)
    product.save()
    return HttpResponse("Product information is saved successfully.")

def _yield_products(products):
    for product in products:
        product_dict = model_to_dict(product)
        product_dict = _convert_date_to_str(product_dict)
        product_json = serialize_data(product_dict)
        yield product_json

def list_products(request):
    products = Product.objects.all()

    products_iter = _yield_products(products)
    return StreamingHttpResponse(products_iter)
