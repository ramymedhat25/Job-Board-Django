from django.db import models

JOB_TYPE=(
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
    )

class Job (models.Model):
    title = models.CharField(max_length=100)
    # location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=15,choices=JOB_TYPE)
    # company = models.CharField(max_length=100)
    # salary = models.IntegerField()
    