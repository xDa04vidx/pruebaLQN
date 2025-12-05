from django.db import models
from .base import AuditModel
from .peliculas import Pelicula
from .planetas import Planeta
from .productores import Productor
from .directores import Director
from .personajes import Personaje


class PeliculaPlaneta(AuditModel):
    pelicula = models.ForeignKey(
        Pelicula,
        on_delete=models.CASCADE,
        db_column="pelicula_id",
        related_name="rel_planetas"
    )
    planeta = models.ForeignKey(
        Planeta,
        on_delete=models.CASCADE,
        db_column="planeta_id",
        related_name="rel_peliculas"
    )

    class Meta:
        db_table = "pelicula_planeta"


class PeliculaProductor(AuditModel):
    pelicula = models.ForeignKey(
        Pelicula,
        on_delete=models.CASCADE,
        db_column="pelicula_id",
        related_name="rel_productores"
    )
    productor = models.ForeignKey(
        Productor,
        on_delete=models.CASCADE,
        db_column="productor_id",
        related_name="rel_peliculas"
    )

    class Meta:
        db_table = "pelicula_productor"


class PeliculaDirector(AuditModel):
    pelicula = models.ForeignKey(
        Pelicula,
        on_delete=models.CASCADE,
        db_column="pelicula_id",
        related_name="rel_directores"
    )
    director = models.ForeignKey(
        Director,
        on_delete=models.CASCADE,
        db_column="director_id",
        related_name="rel_peliculas"
    )

    class Meta:
        db_table = "pelicula_director"


class PeliculaPersonaje(AuditModel):
    pelicula = models.ForeignKey(
        Pelicula,
        on_delete=models.CASCADE,
        db_column="pelicula_id",
        related_name="rel_personajes"
    )
    personaje = models.ForeignKey(
        Personaje,
        on_delete=models.CASCADE,
        db_column="personaje_id",
        related_name="rel_peliculas"
    )

    class Meta:
        db_table = "pelicula_personaje"
