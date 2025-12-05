from django.db import models
from .base import AuditModel


class Planeta(AuditModel):
    nombre = models.CharField(max_length=150)

    class Meta:
        db_table = "planetas"

    def __str__(self):
        return self.nombre
