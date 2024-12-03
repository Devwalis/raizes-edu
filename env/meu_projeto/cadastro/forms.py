from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [ 'nome', 'data_nascimento', 'cpf', 'email', 'password', 'cep', 'uf', 'bairro', 'rua', 'numero',
                  'complemento', 'telefone','tipoUsuario']
        widgets = {
            'data_nascimento': forms.DateInput(attrs ={'type': 'date'}),
            'password': forms.PasswordInput(),
        }
        def clean_cpf(self):
            cpf = self.cleaned_data['cpf']
            if len(cpf) > 12:
                raise forms.ValidationError('O CPF deve ter no máximo 12 caracteres.')
            return cpf

    def clean_cep(self):
        cep = self.cleaned_data['cep']
        if len(cep) > 12:
            raise forms.ValidationError('O CEP deve ter no máximo 12 caracteres.')
        return cep

    def clean_telefone(self):
        telefone = self.cleaned_data['telefone']
        if len(telefone) > 20:
            raise forms.ValidationError('O telefone deve ter no máximo 20 caracteres.')
        return telefone
        
class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
        
