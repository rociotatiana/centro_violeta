from django.contrib import admin

# Register your models here.

from .models import Beneficiaria
admin.site.register(Beneficiaria)


from .models import Region, Provincia, Comuna

admin.site.register(Region)
admin.site.register(Provincia)
admin.site.register(Comuna)

from .models import Comunidad, Programa, Institucion

admin.site.register(Comunidad)
admin.site.register(Programa)
admin.site.register(Institucion)


from .models import Registro_Intervencion

admin.site.register(Registro_Intervencion)


