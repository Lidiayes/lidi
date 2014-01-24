#encoding:utf-8 
from django.forms import ModelForm
from django import forms
from models import User 
from models import Clientes

class ClientesForm(ModelForm):
	class Meta:
		model= Clientes