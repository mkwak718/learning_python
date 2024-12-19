from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import View
from django.template import loader
from django.http import HttpResponse
import sys,io
from .models import *

# Create your views here.
class HomePageView(View):
    def get(self, request):
        context = {} 

        module_titles = PythonModule.objects.filter(published=True).order_by('display_order').values('id', 'title', 'display_order')
        context['module_titles'] = module_titles
        
        return render(request, 'tutorial/home.html', context)

class PythonModuleContentView(View):

    def get(self, request, id):
        context = {} 
        module_content = {}

        module_titles = PythonModule.objects.filter(published=True).order_by('display_order').values('id', 'title', 'display_order')
        if id is None and len(module_titles) > 0:
            id = module_titles[0]['id']        
        
        if id is not None:
            module_content = PythonModule.objects.get(pk=id)
        
        #module_content = get_object_or_404(PythonModule, id = id)

        print(module_titles)
        print(module_content)

        context['module_titles'] = module_titles
        context['module_content'] = module_content
        
        return render(request, 'tutorial/python_content.html', context)

def exec_python_code(request):

    if request.method == 'POST':
        code = request.POST['code']
        __output, __error = None, None

        try:
            tmp = sys.stdout
            new_stdout = io.StringIO(newline=None)
            sys.stdout = new_stdout
            __code = f"""{code}"""
            exec(__code)
            sys.stdout = tmp
            __output = new_stdout.getvalue()
            
        except Exception as _e:
            __error = _e

        result = __error if __error is not None else __output

        return HttpResponse(result)
    else:
        return HttpResponse("Invalid request!")
