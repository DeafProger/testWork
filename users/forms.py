from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import User


class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'is_active',)
