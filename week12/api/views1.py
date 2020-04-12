import json
from django.http.response import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from api.models import Company, Vacancy


@csrf_exempt
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        companies_json = [company.to_json() for company in companies]
        return JsonResponse(companies_json, safe=False)
    elif request.method == 'POST':

        # company = Company(name=request_body.get('name'))
        # company.save()

        request_body = json.loads(request.body)
        new_request = request_body.get('name', 'default name')
        city_name = request_body.get('city', 'default city')
        company = Company.objects.create(name=new_request, city=city_name)
        return JsonResponse(company.to_json())


@csrf_exempt
def company_details(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        raise Http404

    if request.method == 'GET':
        return JsonResponse(company.to_json(), safe=False)
    elif request.method == 'PUT':
        request_body = json.loads(request.body)
        company.name = request_body.get('name', company.name)
        company.save()
        return JsonResponse(company.to_json())
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({'deleted': True})


def company_vacancies(request, company_id):
    vacancies = Vacancy.objects.filter(company=company_id)
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def vacancies_list(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        raise Http404
    return JsonResponse(vacancy.to_json(), safe=False)
