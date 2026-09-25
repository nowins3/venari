from django.forms import ModelForm
from .models import User
from .models import Product

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'password', 'username']