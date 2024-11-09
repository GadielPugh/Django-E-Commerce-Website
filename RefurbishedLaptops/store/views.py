from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, PurchaseForm
from .models import Laptop, Transaction

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
    laptops = Laptop.objects.filter(sold=False)  # Exclude sold laptops
    return render(request, 'store/gallery.html', {'laptops': laptops, 'user': request.user})

# View for laptop details (only for logged-in users)
@login_required
def laptop_detail(request, laptop_id):
    laptop = get_object_or_404(Laptop, id=laptop_id)
    can_purchase = request.user.is_authenticated  # Check if the user is logged in
    return render(request, 'store/laptop_detail.html', {'laptop': laptop, 'can_purchase': can_purchase})

# Purchase view (only for logged-in users)
@login_required
def purchase_laptop(request, laptop_id):
    laptop = get_object_or_404(Laptop, id=laptop_id, sold=False)
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            # Process the purchase form data (simulating payment here)
            transaction = Transaction.objects.create(
                laptop=laptop,
                user=request.user,
                payment_status='completed',  # Marking the payment as complete
                payment_type='debit card'
            )
            # Mark the laptop as sold
            laptop.sold = True
            laptop.save()

            # Redirect to the purchase confirmation page with the transaction id
            return redirect('purchase_confirmation', transaction_id=transaction.id)
    else:
        form = PurchaseForm()

    return render(request, 'store/purchase.html', {'form': form, 'laptop': laptop})

@login_required
def confirm_pickup(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id, user=request.user)
    transaction.confirm_pickup()  # Update the transaction to completed
    return redirect('gallery')  # Redirect to the gallery

def purchase_success(request):
    return render(request, 'store/purchase_success.html')

def custom_logout(request):
    logout(request)
    return redirect('gallery')  # Redirect to the gallery page

def gallery(request):
    laptops = Laptop.objects.all()
    return render(request, 'store/gallery.html', {'laptops': laptops})

def purchase_confirmation(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    return render(request, 'store/purchase_confirmation.html', {'transaction': transaction})

