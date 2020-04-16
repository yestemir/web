from django.db import models


# Create your models here.

class Company(models.Model):
    name = models.TextField(max_length=300)
    description = models.TextField(max_length=600)
    city = models.TextField(max_length=300)
    address = models.TextField(max_length=300)


class Vacancy(models.Model):
    name = models.TextField(max_length=300)
    description = models.TextField(default='')
    salary = models.FloatField(default=0.0)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')

    def __str__(self):
        return f'Vacancies id={self.id}, name={self.name}'

