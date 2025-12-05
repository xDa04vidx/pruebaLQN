from django.db import models

class AuditModel(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario_creacion = models.CharField(max_length=150, default="system")
    fecha_modificacion = models.DateTimeField(null=True, blank=True)
    usuario_modificacion = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        abstract = True
