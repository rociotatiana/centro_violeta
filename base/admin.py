from django.contrib import admin

# Register your models here.

from .models import User, Beneficiaria

admin.site.register(User)
admin.site.register(Beneficiaria)


from .models import Region, Provincia, Comuna

admin.site.register(Region)
admin.site.register(Provincia)
admin.site.register(Comuna)

from .models import Comunidad, Programa, Institucion, Mensaje, Tematica

admin.site.register(Programa)
admin.site.register(Institucion)
admin.site.register(Comunidad)
admin.site.register(Mensaje)
admin.site.register(Tematica)


from .models import Registro_Intervencion, Planilla_Derivacion

admin.site.register(Registro_Intervencion)
admin.site.register(Planilla_Derivacion)


