from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm, CustomAuthenticationForm, UserProfileForm
from .models import User

class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'accounts/login.html'
    
    def get_success_url(self):
        user = self.request.user
        if user.role == 'admin':
            return '/dashboard/'
        elif user.role == 'staff':
            return '/dashboard/orders/'
        elif user.role == 'rider':
            return '/dashboard/'
        else:
            return '/store/'
    
    def form_valid(self, form):
        """Show notifications on login"""
        response = super().form_valid(form)
        # Store a flag to show notifications after redirect
        self.request.session['show_login_notifications'] = True
        return response

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Welcome to Quick Cart! Your account has been created successfully.')
            return redirect('store:product_list')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('accounts:profile')
    else:
        form = UserProfileForm(instance=request.user)
    
    return render(request, 'accounts/profile.html', {'form': form})
