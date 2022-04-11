from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from .forms import EditprofileForm, PaswordChangingForm, SignUpForm
class PasswordChangeView (PasswordChangeView):
    form_class = PaswordChangingForm
    success_url = reverse_lazy('password_success')
    #success_url = reverse_lazy('home')

def password_success (request):
    return render(request, 'registration/password_success.html', {})

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    
class UserEditForm(generic.UpdateView ):
    form_class = EditprofileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('login')
    
    def get_object (self):
        return self.request.user
        