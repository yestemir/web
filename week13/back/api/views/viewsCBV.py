from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import Company
from api.serializers import CompanySerializer2


class CompanyListAPIView(APIView):
    def get(self, request):
        companies = Company.objects.all()
        serializers = CompanySerializer2(companies, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializers = CompanySerializer2(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATE)
        return Response({'error': serializers.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CompanyDetailAPIView(APIView):
    def get_object(self, id):
        try:
            return Company.objects.get(id=id)
        except Company.DoesNotExist as e:
            raise Response({'error': str(e)})

    def get(self, request, company_id):
        company = self.get_object(company_id)
        serializer = CompanySerializer2(company)
        return Response(serializer.data)

    def put(self, request, company_id):
        company = self.get_object(company_id)
        serializer = CompanySerializer2(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.error_messages})

    def delete(self, request, company_id):
        company = self.get_object(company_id)
        company.delete()
        return Response({'deleted': True})