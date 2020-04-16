from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.TextField(max_length=300)
    description = models.TextField(max_length=300)
    city = models.TextField(max_length=300)
    address = models.TextField(max_length=300)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }


class Vacancy(models.Model):
    name = models.TextField(max_length=300)
    description = models.TextField(max_length=300)
    salary = models.FloatField(default=0.0)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary
        }
