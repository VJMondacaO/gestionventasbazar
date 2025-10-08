from django import forms
from .models import Productos, Clientes

class ProductoRegistroForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class ClienteRegistroForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'