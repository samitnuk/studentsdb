from django.shortcuts import render
from django import forms

def contact_admin(request):
    return render(request, 'contact_admin/form.html', {})