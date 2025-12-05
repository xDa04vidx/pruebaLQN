from django.db import models
from .base import AuditModel


class Pelicula(AuditModel):
    title = models.CharField(max_length=150)
    texto_apertra = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "peliculas"

    def __str__(self):
        return self.title
