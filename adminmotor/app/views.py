from django.conf import settings
from django.shortcuts import render_to_response,get_object_or_404, render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template.context import RequestContext
from models import *
from forms import * 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from social.backends.google import GooglePlusAuth


def formas(request):
    #usuarios = User.object.all()
    template="agregar_cliente.html"
    return render_to_response(template,locals())

def home(request):
	#usuarios = User.object.all()
	template="index.html"
	return render_to_response(template,locals())

"""
def nuevo_usuario(request):
    if request.method=='POST':
        formcreateuser = UserCreationForm(request.POST)
        if formcreateuser.is_valid:
            formcreateuser.save()
            return redirect('done')
    else:
        formcreateuser = UserCreationForm()
    return render_to_response('index.html',{'formulario':formcreateuser}, context_instance=RequestContext(request))
"""
def login(request):
    if not request.user.is_anonymous():
        return redirect('done')
    if request.POST:
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return redirect('done')
                else:
                    return render_to_response('noactivo.html', context_instance=RequestContext(request))
            else:
                return render_to_response('nousuario.html', context_instance=RequestContext(request))
    else:
        formulario = AuthenticationForm()
    return render_to_response('index.html',{'formulario':formulario}, context_instance=RequestContext(request))

def logout(request):
    """Logs out user"""
    auth_logout(request)
    return render_to_response('index.html', {}, RequestContext(request))


def home(request):
    """Home view, displays login mechanism"""
    if request.user.is_authenticated():
        return redirect('done')
    return render_to_response('index.html', {
        'plus_id': getattr(settings, 'SOCIAL_AUTH_GOOGLE_PLUS_KEY', None)
    }, RequestContext(request))


@login_required
def done(request):
    """Login complete view, displays user data"""
    scope = ' '.join(GooglePlusAuth.DEFAULT_SCOPE)
    return render_to_response('done.html', {
        'user': request.user,
        'plus_id': getattr(settings, 'SOCIAL_AUTH_GOOGLE_PLUS_KEY', None),
        'plus_scope': scope
    }, RequestContext(request))


def signup_email(request):
    return render_to_response('email_signup.html', {}, RequestContext(request))


def validation_sent(request):
    return render_to_response('validation_sent.html', {
        'email': request.session.get('email_validation_address')
    }, RequestContext(request))


def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')

def add(request):
    cliente=Clientes.objects.all()
    if request.method == "POST" :
        form = ClientesForm(request.POST)
        if form.is_valid():
           form.save()
           return HttpResponseRedirect("/")
    else: 
        form = ClientesForm()
    template = "agregar_cliente.html"
    return render_to_response(template,context_instance = RequestContext(request,locals()))
          

#def Clientesvista(request):
 #   clientes= Clientes.objects.all()
  #  template="index.html"
   # return render_to_response(clientes,locals())

def require_email(request):
    if request.method == 'POST':
        request.session['saved_email'] = request.POST.get('email')
        backend = request.session['partial_pipeline']['backend']
        return redirect('social:complete', backend=backend)
    return render_to_response('email.html', RequestContext(request))

def avanzado(request):
    template="avanzado.html"
    return render_to_response(template,locals())

def basico(request):
    template="basico.html"
    return render_to_response(template,locals())

def contacto(request):
    template="contacto.html"
    return render_to_response(template,locals())

def medio(request):
    template="medio.html"
    return render_to_response(template,locals())

def serviciosinicio(request):
    template="serviciosinicio.html"
    return render_to_response(template,locals())
@login_required
def perfil(request):
    template="perfil.html"
    return render_to_response(template,locals())

@login_required
def paquetebasico(request):
    template="paquetebasico.html"
    return render_to_response(template,locals())
@login_required
def servicios(request):
    template="servicios.html"
    return render_to_response(template,locals())
@login_required
def clientes(request):
    template="clientes.html"
    return render_to_response(template,locals())

@login_required
def altacitas(request):
    template="altacitas.html"
    return render_to_response(template,locals())

@login_required
def altaproveedores(request):
    template="altaproveedores.html"
    return render_to_response(template,locals())
@login_required
def altaclientes(request):
    template="altaclientes.html"
    return render_to_response(template,locals())
@login_required
def altavehiculo(request):
    template="altavehiculo.html"
    return render_to_response(template,locals())
@login_required
def vehiculo(request):
    template="vehiculo.html"
    return render_to_response(template,locals())
@login_required
def altacompra(request):
    template="altacompra.html"
    return render_to_response(template,locals())
@login_required
def altausuario(request):
    template="altausuario.html"
    return render_to_response(template,locals())
@login_required
def altaempleado(request):
    template="altaempleado.html"
    return render_to_response(template,locals())
@login_required
def altaservicio(request):
    template="altaservicio.html"
    return render_to_response(template,locals())
@login_required
def altaproducto(request):
    template="altaproducto.html"
    return render_to_response(template,locals())
@login_required
def altaventa(request):
    template="altaventa.html"
    return render_to_response(template,locals())
@login_required
def consultaclientes(request):
    template="consultaclientes.html"
    return render_to_response(template,locals())