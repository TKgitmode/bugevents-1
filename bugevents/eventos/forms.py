from datetime import date

from django.forms import ModelForm, TextInput
from django.core.exceptions import ValidationError

from .models import Ambiente, Evento, Turno, Material


'''
EventoForm -> Creacion, modificacion y validacion de Eventos
Clase relacionada -> CD85 [Control]
Casos de Uso relacionados -> {BE04, BE05}
'''
class EventoForm(ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'

    def clean(self):
        fecha_inicio = self.cleaned_data.get('fecha_inicio')
        fecha_fin = self.cleaned_data.get('fecha_fin')
        if fecha_inicio <= date.today():
            raise ValidationError("Los eventos no pueden iniciar en el pasado ni en el día en que se crean.")
        if fecha_inicio > fecha_fin:
            raise ValidationError("La fecha de inicio no puede ser posterior a la fecha de fin.")


'''
AmbienteForm -> Creacion, modificacion y validacion de Ambientes
Clase relacionada -> CD25 [Control]
Casos de Uso relacionados -> {BE07, BE08}
'''
class AmbienteForm(ModelForm):
    class Meta:
        model = Ambiente
        fields = '__all__'
        widgets = {
            'aforo': TextInput(attrs={"type": "number",
                                      "min": "1"})
        }

    def clean(self):
        aforo = self.cleaned_data.get('aforo')
        if aforo <= 0:
            raise ValidationError("El valor de aforo debe ser un número positivo.")


'''
TurnoForm -> Formulario de creacion de Turnos
Clase relacionada -> CD45 [Control]
Casos de Uso relacionados -> {BE12}
'''
class TurnoForm(ModelForm):
    class Meta:
        model = Turno
        fields = '__all__'

    def clean(self):
        hora_inicio = self.cleaned_data.get('hora_inicio')
        hora_fin = self.cleaned_data.get('hora_fin')
        if hora_inicio > hora_fin:
            raise ValidationError("La hora de inicio no puede ser posterior a la hora de fin.")
'''
MaterialForm -> Formulario de creacion, modificacion y validacion de Materiales
clase relacionada -> CD46 [Control]
Casos de uso relacionados -> {BE13, BE14}
'''
class MaterialForm(ModelForm):
    class Meta:
        model = Material
        fields = '__all__'
        widgets = {
            'cantidad': TextInput(attrs={"type": "number",
                                      "min": "1"})
        }

    def clean(self):
        descripcion = self.cleaned_data.get('descripcion')
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad <= 0:
            raise ValidationError("La cantidad debe ser un número mayor a 0.") 
