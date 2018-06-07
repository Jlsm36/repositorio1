from django.shortcuts import render

# Create your views here.
from .forms import RegForm  #muy importante para importar el formulario
from .models import Registrado
# Create your views here.

# Create your views here.
# Las vistas manejan los requests de los usuarios

# nueva funcion
def hola(request):
    """
    Devuelve un mensaje.
    La función render toma un parámetro formal context, el cual es un diccionario formado por
    una key “mensaje” y valor “Hola Mundo”.
    Dentro del template (hola.html) vamos a poder acceder mediante las keys del contexto a sus valores.
    """
    return render(request, 'hola.html', context={"mensaje": "Hola Mundo"})


def inicio(request):
    return render(request, 'inicio.html', context={})  # contexto un diccionario vacío


def saludo(request):
    #form = RegForm()
    form = RegForm(request.POST or None) #sin pinchar el boton registrame ya nos indica que los campos son obligatorios por el modelo es incomodo por ello incluimos None
    #print(dir(form))  truco para atributos y métodos del form
    if form.is_valid():
        print(form.cleaned_data)  #datos limpios del formulario que se puede ver el diccionario en unicode en la consola
        form_data=form.cleaned_data
        print(form_data.get("nombre"))  #recupera con metodo GET
        #print(form_data.get("edad"))  #recupera con metodo GET

        correo=form_data.get("email")
        nom=form_data.get("nombre")
        obj= Registrado.objects.create(email=correo, nombre=nom) #ya guarda en la tabla de la BD  (Blank es para formulario y Null para la tabla)

        #otra forma de hacer las tres lineas anteriores
        '''
        obj=Registrado()
        obj.email=correo
        obj.nombre=nom
        obj.save()
        '''

    #el diccionario asociado al contexto. el_form es la variable de la plantilla
    context = {
        "el_form": form,
    }
    return render(request, 'saludo.html', context)
