from django.forms import ModelForm
from social.models import UserInfo, Picture
from django.contrib.auth.models import User

# class UserModelForm(ModelForm):
#     class Meta:
#         model = UserInfo
#         fields = [ 'website']
        
#         # 'username', 'email', 'first_name', 'last_name', 'biography', , 'gender', 'phone_country_code', 'phone_number', 'privacy'

class UserForm(ModelForm):
    class Meta:
        model = User
        exclude = ['password','last_login','is_superuser','is_staff','date_joined','groups','user_permissions']
        # fields = ('__all__')
        
    # def save(self, user=None):
    #     user_info = super(UserInfoForm, self).save(commit=False)
    #     # if user:
    #     #     user_info.user = user
    #     user_info.save()
    #     return user_info
    
class PictureForm(ModelForm):

    class Meta: 
        model = Picture
        fields = ['picture_description', 'picture'] 