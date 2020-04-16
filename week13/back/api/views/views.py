import json

from django.shortcuts import render
from django.http.response import JsonResponse, Http404

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from api.models import Company
from api.serializers import CompanySerializer


@csrf_exempt
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializers = CompanySerializer(companies, many=True)
        return JsonResponse(serializers.data, safe=False)
    elif request.method == 'POST':
        request_body = json.loads(request.body)
        serializers = CompanySerializer(data=request_body)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data)
        return JsonResponse({'error': serializers.errors})


@csrf_exempt
def company_details(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        raise Http404

    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        request_body = json.loads(request.body)
        serializer = CompanySerializer(instance=company, data=request_body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'error': serializer.error_messages})
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({'deleted': True})
