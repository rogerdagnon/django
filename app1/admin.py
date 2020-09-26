from django.contrib import admin

# Register your models here.
from app1.models import Topico, RegistroAcesso, Webpage, Model, DadosForm

admin.site.register(Topico)
admin.site.register(RegistroAcesso)
admin.site.register(Webpage)
admin.site.register(Model)
admin.site.register(DadosForm)
