from django.shortcuts import render
from django.http.response import JsonResponse, Http404
from api.models import Products, Categories


def product_list(request):
    products = Products.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)


# Create your views here.


def getproduct(request, product_id):
    try:
        product = Products.objects.get(id=product_id)
    except Products.DoesNotExist as e:
        raise Http404
    return JsonResponse(product.to_json())


def category_list(request):
    categories = Categories.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False)


def getcategory(request, category_id):
    try:
        category = Categories.objects.get(id=category_id)
    except Products.DoesNotExist as e:
        raise Http404
    return JsonResponse(category.to_json())


def getproductsbycategory(request, category_id):
    products = Products.objects.filter(category=category_id)
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)
