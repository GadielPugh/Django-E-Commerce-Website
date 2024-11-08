from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from .models import UserProfile

# Views fpr remder 
from .models import Laptop
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


# Registration View
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Save additional fields if needed
            user.profile.address = form.cleaned_data.get('address')
            user.profile.bank_details = form.cleaned_data.get('bank_details')
            user.profile.save()
            login(request, user)
            return redirect('gallery')  # redirect to a page after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'store/register.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home page after login
    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {'form': form})

# View for the laptop gallery (accessible to everyone)
def laptop_gallery(request):
    laptops = Laptop.objects.filter(is_sold=False)
    return render(request, 'store/gallery.html', {'laptops': laptops})

# View for laptop details (only for logged-in users)
@login_required
def laptop_detail(request, id):
    laptop = get_object_or_404(Laptop, id=id)
    return render(request, 'store/laptop_detail.html', {'laptop': laptop})

# Purchase view (only for logged-in users)
@login_required
def purchase_laptop(request, id):
    laptop = get_object_or_404(Laptop, id=id)
    # Logic to handle the purchase
    # (e.g., create a Transaction record or flag the laptop as sold)
    return redirect('gallery')