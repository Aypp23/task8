from django.shortcuts import render, redirect
from .models import  Guest

# Create your views here.

def ManagementPage(request):
    if request.method == 'POST':
        guest = Guest.objects.create(
            guest_name = request.POST.get('guest_name'),
            guest_email = request.POST.get('guest_email'),
            guest_occupation = request.POST.get('guest_occupation'),
            number_of_nights = request.POST.get('nights'),
            start_date = request.POST.get('start_date'),
            end_date = request.POST.get('end_date'),    
            room_number = request.POST.get('room_number'),
            amount = request.POST.get('room_amount'),
        )


        return redirect('management')
    return render(request, 'management/index.html')

        
