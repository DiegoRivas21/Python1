from django.contrib import admin

# Register your models here.
from .models import Etnia
from .models import TipoDocu
from .models import EstaCivil
from .models import TipoEstu
from .models import TipoLogr

admin.site.register (Etnia)
admin.site.register(TipoDocu)
admin.site.register(EstaCivil)
admin.site.register(TipoEstu)
admin.site.register(TipoLogr)