from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Review, User


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['item_name', 'description', 'rating']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio']
