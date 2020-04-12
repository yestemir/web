from django.urls import path
#from api.views import company_list, company_details, company_vacancies, vacancies_list, vacancy_detail
from api.views import company_list, company_details

urlpatterns = [
    path('companies/', company_list),
    path('companies/<int:company_id>/', company_details),
    #path('companies/<int:company_id>/vacancies/', company_vacancies),
    #path('vacancies/', vacancies_list),
    #path('vacancies/<int:vacancy_id>', vacancy_detail)
]
