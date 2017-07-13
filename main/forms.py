from registration.forms import RegistrationForm
from .models import Petal


class PetalForm(RegistrationForm):
    class Meta:
        model = Petal
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
