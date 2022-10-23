from django import forms

class HumanoFormulario(forms.Form):
    nombre = forms.CharField(max_lenght=30)
    apellido = forms.CharField(max_lenght=30)
    edad = forms.IntegerField()
    fecha_creacion = forms.DateField(required=False)