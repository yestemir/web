
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.models import Company
from api.serializers import CompanySerializer2


@api_view(['GET', 'POST'])
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializers = CompanySerializer2(companies, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializers = CompanySerializer2(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATE)
        return Response({'error': serializers.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
def company_details(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        raise Response({'error': str(e)})

    if request.method == 'GET':
        serializer = CompanySerializer2(company)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CompanySerializer2(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.error_messages})
    elif request.method == 'DELETE':
        company.delete()
        return Response({'deleted': True})
