from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def func_template_(request):
    return render(request, 'func_template.html')


class class_teamplate_(TemplateView):
    template_name = 'class_template.html'
