import os
from dotenv import load_dotenv
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from django.core.mail import send_mail
from .forms import UserRegisterForm
from users.models import CustomUser

load_dotenv(override=True)

class RegisterView(CreateView):
    model = CustomUser
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('catalogs:home_2')

    def form_valid(self, form):
        user = form.save()
        self.send_welcome_mail(user.email)

        return super().form_valid(form)

    def send_welcome_mail(self, user_email):
        subject = "Добро пожаловать!"
        message = "Правильно сделали, что зарегистрировались!"
        from_email = os.getenv("EMAIL_HOST_USER")
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)










