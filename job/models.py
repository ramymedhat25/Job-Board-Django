from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

JOB_TYPE=(
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
    )

class Job (models.Model):
    title = models.CharField(max_length=100)
    # location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=15,choices=JOB_TYPE)
    Description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    Salary = models.IntegerField(default=0)
    Experience = models.IntegerField(default=1)
    Category = models.ForeignKey('Category',on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


