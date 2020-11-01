from django.contrib import admin

from .models import Ambiente, Evento, Actividad, Ponente, Turno, Material
from .forms import AmbienteForm, EventoForm, TurnoForm, MaterialForm

class AmbienteAdmin(admin.ModelAdmin):
    form = AmbienteForm
admin.site.register(Ambiente, AmbienteAdmin)

class EventoAdmin(admin.ModelAdmin):
    form = EventoForm
admin.site.register(Evento, EventoAdmin)

admin.site.register(Actividad)

admin.site.register(Ponente)

class TurnoAdmin(admin.ModelAdmin):
    form = TurnoForm
admin.site.register(Turno, TurnoAdmin)

class MaterialAdmin(admin.ModelAdmin):
    form = MaterialForm
admin.site.register(Material,MaterialAdmin)