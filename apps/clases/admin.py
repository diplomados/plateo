from django.contrib import admin
from .models import Curso, Docente
# Register your models here.


class CursoAdmin(admin.ModelAdmin):

    search_fields = ('nombre',)
    list_filter = (
        ('slug'),
    )
    # https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.prepopulated_fields
    list_display = ('nombre', 'slug', 'usuario',)
    list_per_page = 3

    ordering = ('-nombre', )
    exclude = ['usuario', 'slug']

    filter_horizontal = ('docente',)  # must be a ManyToManyField.
    # radio_fields = {"idioma": admin.HORIZONTAL,'medio_pago': admin.VERTICAL}
    # #ForeignKey

    def save_model(self, request, obj, form, change):
        if not obj.usuario_id:
            obj.usuario = request.user
        obj.save()

admin.site.register(Curso, CursoAdmin)

admin.site.register(Docente)