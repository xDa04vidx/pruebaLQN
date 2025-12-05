from django.db import models
from .base import AuditModel
from .planetas import Planeta


class Personaje(AuditModel):
    nombre = models.CharField(max_length=100)
    planeta = models.ForeignKey(
        Planeta,
        on_delete=models.CASCADE,
        db_column="planeta_id",
        related_name="personajes"
    )

    class Meta:
        db_table = "personajes"

    def __str__(self):
        return self.nombre
