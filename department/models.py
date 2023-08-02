from django.db import models

from branch.models import Branch


class Department(models.Model):
    name = models.CharField(max_length=100)
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.name