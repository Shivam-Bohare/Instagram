from django.forms import ModelForm
from social.models import User

class UserModelForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']