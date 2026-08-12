from django.urls import reverse_lazy

from django.views.generic import FormView

from .forms import UserRegisterForm
from users.models import CustomUser

class RegisterView(FormView):
    model = CustomUser
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('catalogs:home_2')







