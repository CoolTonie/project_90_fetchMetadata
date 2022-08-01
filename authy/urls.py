from re import template
from tokenize import Name
from unicodedata import name
from django.urls import path, include
from authy.views import UserProfile, EditProfile
from django_registration.backends.activation.views import RegistrationView
from .forms import AuthyRegistrationForm



urlpatterns = [
   	
    path('profile/edit', EditProfile, name='edit-profile'),
	path('accounts/profile/', UserProfile, name='profile'),
	path("accounts/signup/", RegistrationView.as_view(form_class=AuthyRegistrationForm), name="signup"),
	path("accounts/", include("allauth.urls")),
	path('accounts/', include('django.contrib.auth.urls')),
	

	path("accounts/", include("django_registration.backends.activation.urls"))




]