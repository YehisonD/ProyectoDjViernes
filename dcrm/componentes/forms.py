from django import forms
from django.core.validators import RegexValidator
from .models import Componente

# Regex Validators for security and structure
safe_name = RegexValidator(
    r'^[a-zA-Z0-9\s\-\.\#\(\)\/]+$',
    "El nombre del componente solo debe contener letras, números, espacios y caracteres básicos (- . # () /)."
)
safe_spec = RegexValidator(
    r'^[a-zA-Z0-9\s\-\.\,\#\(\)\/\:\;\@\%\+\*]+$',
    "Las especificaciones solo deben contener texto, números y caracteres básicos."
)

class ComponenteForm(forms.ModelForm):
    nombre = forms.CharField(
        label="",
        validators=[safe_name],
        widget=forms.TextInput(attrs={
            "placeholder": "Nombre del componente",
            "class": "form-control",
            "pattern": "^[a-zA-Z0-9\\s\\-\\.\\#\\(\\)\\/]+$"
        })
    )
    categoria = forms.ChoiceField(
        label="",
        choices=[('', 'Seleccionar categoría...')] + Componente.CATEGORIA_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"})
    )
    especificacion = forms.CharField(
        label="",
        validators=[safe_spec],
        widget=forms.TextInput(attrs={
            "placeholder": "Ej: 6 núcleos, 3.7GHz, 65W",
            "class": "form-control",
            "pattern": "^[a-zA-Z0-9\\s\\-\\.\\,\\#\\(\\)\\/\\:\\;\\@\\%\\+\\*]+$"
        })
    )
    gama = forms.ChoiceField(
        label="",
        choices=Componente.GAMA_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"})
    )
    precio = forms.DecimalField(
        label="",
        widget=forms.NumberInput(attrs={
            "placeholder": "Precio",
            "class": "form-control",
            "min": "0",
            "step": "0.01"
        })
    )
    stock = forms.IntegerField(
        label="",
        required=False,
        initial=0,
        widget=forms.NumberInput(attrs={
            "placeholder": "Stock inicial",
            "class": "form-control",
            "min": "0"
        })
    )

    class Meta:
        model = Componente
        fields = ["nombre", "categoria", "especificacion", "gama", "precio", "stock"]
