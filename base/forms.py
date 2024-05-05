from django.forms import ModelForm
#from django.contrib.auth.forms import UserCreationForm
from .models import Registro_Intervencion, Beneficiaria, Planilla_Derivacion, Comunidad


class IntervencionForm(ModelForm):
    class Meta:
        model = Registro_Intervencion
        fields = '__all__'

class BeneficiariaForm(ModelForm):
    class Meta:
        model = Beneficiaria
        fields = '__all__'

class DerivacionForm(ModelForm):
    class Meta:
        model = Planilla_Derivacion
        fields = '__all__'
        
class ComunidadForm(ModelForm):
    class Meta:
        model = Comunidad
        fields = '__all__'
#class MyUserCreationForm(UserCreationForm):
#    class Meta:
#        model = User
#        fields = ['name', 'username', 'email', 'password1', 'password2']


class Form(ModelForm):
    class Meta:
        model = Registro_Intervencion
        fields = '__all__'
        exclude = ['host', 'participants']


#class UserForm(ModelForm):
#    class Meta:
#        model = User
#        fields = ['avatar', 'name', 'username', 'email', 'bio']