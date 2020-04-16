from django.urls import path

#from api.views import company_list, company_details
#from api.views.viewsCBV import CompanyListAPIView
#from api.views.viewsGeneric import CompanyListAPIView, CompanyDetailAPIView
#from api.views.viewsGeneric2 import CompanyListAPIView, CompanyDetailAPIView, VacancyListAPIView, \
    #VacancyDetailAPIView
#from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import obtain_jwt_token

from api.views2.cbvView import CompanyList, VacancyList, CompanyVacancies, VacancyDetails, CompanyDetails
urlpatterns = [
    #path('companies/', company_list),
    #path('companies/<int:company_id>/', company_details)

    #path('companies/', CompanyListAPIView.as_view())
    #path('companies/<int:company_id>/', CompanyDetailAPIView.as_view())

    # path('companies/', company_list),
    # path('companies/<int:company_id>/', company_details),
    # path('companies/<int:company_id>/vacancies/', CompanyVacanciesAPIView.as),
    # path('vacancies/', vacancies_list),
    # path('vacancies/<int:vacancy_id>', vacancy_detail),
    # path('vacancies/top_ten', top_ten),

    # path('login/', obtain_jwt_token),

    # path('companies/', CompanyListAPIView.as_view()),
    # path('companies/<int:pk>/', CompanyDetailAPIView.as_view()),
    #
    # path('vacancies/', VacancyListAPIView.as_view()),
    # path('vacancies/<int:pk>/', VacancyDetailAPIView.as_view()),

    path('login/', obtain_jwt_token),
    path('companies/', CompanyList.as_view()),
    path('companies/<int:pk>/', CompanyDetails.as_view()),
    path('companies/<int:company_id>/vacancies/', CompanyVacancies.as_view()),
    path('vacancies/', VacancyList.as_view()),
    path('vacancies/<int:pk>/', VacancyDetails.as_view())

   # path('companies/<int:company_id>/vacancies/', CompanyVacanciesAPIView.as_view()),
]