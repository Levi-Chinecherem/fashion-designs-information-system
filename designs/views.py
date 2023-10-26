# designs/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Design, Client
from .forms import DesignForm, ClientForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

def home(request):
    return render(request, 'designs/home.html')

@login_required
def upload_design(request):
    if request.method == 'POST':
        form = DesignForm(request.POST, request.FILES)
        if form.is_valid():
            design = form.save(commit=False)
            design.designer = request.user
            design.save()
            return redirect('design_list')
    else:
        form = DesignForm()
    return render(request, 'designs/upload_design.html', {'form': form})

@login_required
def design_list(request):
    designs = Design.objects.filter(designer=request.user)
    return render(request, 'designs/design_list.html', {'designs': designs})

@login_required
def manage_client_info(request):
    client, created = Client.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
    else:
        form = ClientForm(instance=client)
    return render(request, 'designs/manage_client_info.html', {'form': form})

@login_required
def design_detail(request, design_id):
    design = get_object_or_404(Design, id=design_id, designer=request.user)
    return render(request, 'designs/design_detail.html', {'design': design})

@login_required
def update_design(request, design_id):
    design = get_object_or_404(Design, id=design_id, designer=request.user)

    if request.method == 'POST':
        form = DesignForm(request.POST, request.FILES, instance=design)
        if form.is_valid():
            form.save()
            return redirect('design_list')
    else:
        form = DesignForm(instance=design)
    return render(request, 'designs/update_design.html', {'form': form, 'design': design})

@login_required
def delete_design(request, design_id):
    design = get_object_or_404(Design, id=design_id, designer=request.user)

    if request.method == 'POST':
        design.delete()
        return redirect('design_list')

    return render(request, 'designs/delete_design.html', {'design': design})
