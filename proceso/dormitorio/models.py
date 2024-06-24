from django.db import models

from proceso.edificio.models import Edificio


# Create your models here.


class Dormitorio(models.Model):
    codigo = models.CharField(max_length=15,verbose_name="codigo", unique=True)
    edificioID = models.ForeignKey(Edificio, on_delete=models.DO_NOTHING, verbose_name='edificio', related_name='dormitorios')

    def __str__(self):
        return self.codigo