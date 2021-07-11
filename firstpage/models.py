
from django.db import models


class Main(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name + " | " + str(self.pk)
