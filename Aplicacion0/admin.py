from django.contrib import admin

# Register your models here.
from .models import Registrado

class AdminRegistrado(admin.ModelAdmin):
        #todos son listas []
        #list_display=[]
        #list_display = ["__unicode__","nombre","timestamp"]
        list_display = ["email", "nombre", "timestamp"] #la lista de campos o columnas a mostrar en el backend de admin
        #list_display_links=["nombre"]  #no interesa que el email que es link sea editable es incómodo
        list_filter=["timestamp"]   #el campo a usar como filtro
        list_editable=["nombre"]  #email no vale porque es el enlace y el enlace no es editable solo podemos cambiar el nombre en este caso
        search_fields=["email", "nombre"]  #busca por estos dos campos
        class Meta:
            model= Registrado
admin.site.register(Registrado, AdminRegistrado)  #registrar el modelo en admin
