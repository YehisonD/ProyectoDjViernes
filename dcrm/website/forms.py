# dcrm/website/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from .models import Record

# Regular Expression Validators for Security & Validation
letters_only = RegexValidator(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', "Solo se permiten letras y espacios en este campo.")
phone_regex = RegexValidator(r'^\d{10}$', "Solo se permiten números y deben ser exactamente 10 números.")
zip_regex = RegexValidator(r'^\d{4,8}$', "El código postal debe contener entre 4 y 8 dígitos numéricos.")
safe_username = RegexValidator(r'^[a-zA-Z0-9_.]+$', "El usuario solo debe contener letras, números, puntos (.) y guiones bajos (_).")
safe_password = RegexValidator(r'^[a-zA-Z0-9@#$.%*?&!]+$', "La contraseña solo debe contener letras, números y caracteres seguros (@#$.%*?&!). Evite comillas y caracteres especiales peligrosos.")

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={"placeholder": "Correo electronico", "class": "form-control"}))
    first_name = forms.CharField(label="", validators=[letters_only], widget=forms.TextInput(attrs={"placeholder": "Nombre", "class": "form-control", "pattern": "^[a-zA-ZáéíóúÁÉÍÓÚñÑ\\s]+$"}))
    last_name = forms.CharField(label="", validators=[letters_only], widget=forms.TextInput(attrs={"placeholder": "Apellido", "class": "form-control", "pattern": "^[a-zA-ZáéíóúÁÉÍÓÚñÑ\\s]+$"}))
    phone = forms.CharField(label="", validators=[phone_regex], widget=forms.TextInput(attrs={"placeholder": "Teléfono", "class": "form-control", "pattern": "^\\d{10}$"}), required=False)
    address = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": "Dirección", "class": "form-control"}), required=False)
    city = forms.CharField(label="", validators=[letters_only], widget=forms.TextInput(attrs={"placeholder": "Ciudad", "class": "form-control", "pattern": "^[a-zA-ZáéíóúÁÉÍÓÚñÑ\\s]+$"}), required=False)
    state = forms.CharField(label="", validators=[letters_only], widget=forms.TextInput(attrs={"placeholder": "Estado", "class": "form-control", "pattern": "^[a-zA-ZáéíóúÁÉÍÓÚñÑ\\s]+$"}), required=False)
    zip_code = forms.CharField(label="", validators=[zip_regex], widget=forms.TextInput(attrs={"placeholder": "Código Postal", "class": "form-control", "pattern": "^\\d{4,8}$"}), required=False)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        # Enforce validation and pattern for built-in UserCreationForm fields
        self.fields["username"].validators.append(safe_username)
        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["placeholder"] = "Nombre de usuario"
        self.fields["username"].widget.attrs["pattern"] = "^[a-zA-Z0-9_.]+$"
        self.fields["username"].label = ""
        self.fields["username"].help_text = (
            '<span class="form-text text-muted">Requerido. 150 caracteres o menos. '
            "Letras, digitos, puntos y guión bajo solamente.</span>"
        )

        self.fields["password1"].validators.append(safe_password)
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["placeholder"] = "Contraseña"
        self.fields["password1"].widget.attrs["pattern"] = "^[a-zA-Z0-9@#$.%*?&!]+$"
        self.fields["password1"].label = ""
        self.fields["password1"].help_text = (
            '<ul class="form-text text-muted">'
            "<li>Tu contraseña no puede contener caracteres especiales peligrosos (evita comillas).</li>"
            "<li>Tu contraseña debe contener al menos 8 caracteres.</li>"
            "<li>Tu contraseña no puede ser una contraseña común.</li>"
            "<li>Tu contraseña no puede ser completamente numérica.</li>"
            "</ul>"
        )

        self.fields["password2"].validators.append(safe_password)
        self.fields["password2"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirmar contraseña"
        self.fields["password2"].widget.attrs["pattern"] = "^[a-zA-Z0-9@#$.%*?&!]+$"
        self.fields["password2"].label = ""
        self.fields["password2"].help_text = (
            '<span class="form-text text-muted">Requerido. Debe coincidir con la contraseña anterior.</span>'
        )

class RecordForm(forms.ModelForm):
    first_name = forms.CharField(label="", validators=[letters_only], widget=forms.TextInput(attrs={"placeholder": "Nombre", "class": "form-control", "pattern": "^[a-zA-ZáéíóúÁÉÍÓÚñÑ\\s]+$"}))
    last_name = forms.CharField(label="", validators=[letters_only], widget=forms.TextInput(attrs={"placeholder": "Apellido", "class": "form-control", "pattern": "^[a-zA-ZáéíóúÁÉÍÓÚñÑ\\s]+$"}))
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={"placeholder": "Email", "class": "form-control"}))
    phone_number = forms.CharField(
        label="",
        validators=[phone_regex],
        widget=forms.TextInput(attrs={"placeholder": "Telefono", "class": "form-control", "pattern": "^\\d{10}$"}),
    )
    address = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": "Direccion", "class": "form-control"}))
    city = forms.CharField(label="", validators=[letters_only], widget=forms.TextInput(attrs={"placeholder": "Ciudad", "class": "form-control", "pattern": "^[a-zA-ZáéíóúÁÉÍÓÚñÑ\\s]+$"}))
    state = forms.CharField(label="", validators=[letters_only], widget=forms.TextInput(attrs={"placeholder": "Estado", "class": "form-control", "pattern": "^[a-zA-ZáéíóúÁÉÍÓÚñÑ\\s]+$"}))
    zip_code = forms.CharField(
        label="",
        validators=[zip_regex],
        widget=forms.TextInput(attrs={"placeholder": "Codigo Postal", "class": "form-control", "pattern": "^\\d{4,8}$"}),
    )

    class Meta:
        model = Record
        fields = ["first_name", "last_name", "email", "phone_number", "address", "city", "state", "zip_code"]