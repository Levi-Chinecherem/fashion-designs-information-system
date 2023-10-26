# scheduling/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Appointment
from .forms import AppointmentForm, ContactForm
from .models import Availability
from django.contrib.auth.models import User

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()
    
    return render(request, 'scheduling/contact_us.html', {'form': form})

def contact_success(request):
    return render(request, 'scheduling/contact_success.html')

def view_available_slots(request):
    available_slots = Availability.objects.all()
    return render(request, 'scheduling/available_slots.html', {'available_slots': available_slots})

@login_required
def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.client = request.user
            appointment.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
        form.fields['designer'].queryset = User.objects.filter(groups__name='Designer')  # Filter users in the 'Designer' group
    return render(request, 'scheduling/create_appointment.html', {'form': form})

@login_required
def appointment_list(request):
    appointments = Appointment.objects.filter(client=request.user)
    return render(request, 'scheduling/appointment_list.html', {'appointments': appointments})

@login_required
def update_appointment(request, appointment_id):
    appointment = Appointment.objects.get(pk=appointment_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'scheduling/update_appointment.html', {'form': form, 'appointment': appointment})

@login_required
def delete_appointment(request, appointment_id):
    appointment = Appointment.objects.get(pk=appointment_id)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_list')
    return render(request, 'scheduling/delete_appointment.html', {'appointment': appointment})
