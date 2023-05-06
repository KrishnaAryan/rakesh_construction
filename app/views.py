from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import *
# Create your views here.

def index(request):
    
    #form
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page') # redirect to a success page
    else:
        form = CustomerForm()
    
    #  View our latest projects.
    projects=LatestProject.objects.all()   
    context={
        'form': form,
        'projects':projects,
    }
    
    return render(request, 'index.html', context)

def success_page(request):
    return render(request, 'success_page.html')

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



def blog_single(request):
    return render(request, 'blog-single.html')

def projects_single(request, pk):
    poject_view=LatestProject.objects.get(pk=pk)
    context={
        'poject_view':poject_view
    }
    return render(request, 'projects-single.html', context)

def team_single(request):
    return render(request, 'team-single.html')


