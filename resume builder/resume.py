
from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)

from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'

from django.shortcuts import render
from .forms import ResumeForm
from reportlab.pdfgen import canvas
from django.http import HttpResponse

def generate_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
           
            name = form.cleaned_data['name']
            designation = form.cleaned_data['designation']

            
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{name}_resume.pdf"'

            p = canvas.Canvas(response)
           
            p.drawString(100, 800, f"Resume for {name}")
            p.drawString(100, 780, f"Designation: {designation}")

          
            p.showPage()
            p.save()

            return response
    else:
        form = ResumeForm()

    return render(request, 'generate_resume.html', {'form': form})
<!-- ResumeApp/templates/generate_resume.html -->
<form method="post" action="{% url 'generate_resume' %}">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Generate Resume</button>
</form>

from django.urls import path
from .views import generate_resume

urlpatterns = [
    path('generate_resume/', generate_resume, name='generate_resume'),
]

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ResumeApp.urls')),
]
