from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from django.template import defaultfilters
# Create your models here.


class Docente(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = _('Docente')
        verbose_name_plural = _('Docente')

    def __unicode__(self):
        return self.nombre


class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    slug = models.CharField(max_length=50, null=True, blank=True)
    usuario = models.ForeignKey(User)
    docente = models.ManyToManyField(Docente, null=True, blank=True)

    class Meta:
        verbose_name = _('Curso')
        verbose_name_plural = _('Cursos')

    def __unicode__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.nombre)
        # http://django.es/blog/slugs-en-urls/
        super(Curso, self).save(*args, **kwargs)
