from django.contrib.auth.forms import UserCreationForm,  AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = "all"


class CustomAuthenticationForm(AuthenticationForm):
    pass





