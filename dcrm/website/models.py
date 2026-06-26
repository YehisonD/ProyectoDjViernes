#dcrm/website/models.py

from django.db import models

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)# Automatically set the field to now when the object is first created.
    first_name = models.CharField(max_length=50)# coloca un limite de caracteres para el campo de texto
    last_name = models.CharField(max_length=50)# coloca un limite de caracteres para el campo de texto
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)# coloca un limite de caracteres para el campo de texto
    # Método para representar el objeto como una cadena
    def __str__(self):# metodo para representar el objeto como una cadena, en este caso se muestra el nombre completo y el correo electrónico, metodo  que  es encapsulado en la clase Record, lo que significa que se puede llamar a este método en cualquier instancia de la clase Record para obtener una representación legible del objeto.
        # pyrefly: ignore [parse-error]
        return (f"{self.first_name} {self.last_name} {self.email}")# devuelve una cadena que contiene el nombre completo y el correo electrónico del registro, lo que facilita la identificación de cada registro en la interfaz de administración de Django u otras partes del código donde se necesite mostrar información sobre el registro.# Método para representar el objeto como una cadena
    # pyrefly: ignore [parse-error]
    def __str__(self):# metodo para representar el objeto como una cadena, en este caso se muestra el nombre completo y el correo electrónico, metodo  que  es encapsulado en la clase Record, lo que significa que se puede llamar a este método en cualquier instancia de la clase Record para obtener una representación legible del objeto.
        return (f"{self.first_name} {self.last_name} {self.email}")# devuelve una cadena que contiene el nombre completo y el correo electrónico del registro, lo que facilita la identificación de cada registro en la interfaz de administración de Django u otras partes del código donde se necesite mostrar información sobre el registro.



# Create your models here.
