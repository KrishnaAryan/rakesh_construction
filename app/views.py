from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def services(request):
    return render(request, 'services.html')

def general_construction(request):
    return render(request, 'general-construction.html')

def property_maintenance(request):
    return render(request, 'property-maintenance.html')

def project_managment(request):
    return render(request, 'project-managment.html')

def virtual_design_build(request):
    return render(request, 'virtual-design-build.html')

def preconstruction(request):
    return render(request, 'preconstruction.html')

def design_build(request):
    return render(request, 'design-build.html')


