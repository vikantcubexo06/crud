from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crud.models import Information, Profile


class UserForm(forms.ModelForm):
    class Meta:
        fields = ['User_name', 'First_name', 'Last_name', 'Email', 'Age']
        # fields = '__all__'
        model = Information


# class RegistrationForm(UserCreationForm):
#
#     class meta:
#         model = CreateUser
#         field = ['email','password','first_name','last_name']


# class RegistrationForm(UserCreationForm):
#     first_name = forms.CharField(max_length=30)
#     last_name = forms.CharField(max_length=30)
#     email = forms.EmailField(max_length=75)
#
#     class Meta:
#         model = User
#         fields = "__all__"
#
#     def save(self, commit=True):
#         user = super(RegistrationForm, self).save(commit=False)
#         user.first_name = self.cleaned_data["first_name"]
#         user.last_name = self.cleaned_data["last_name"]
#         user.email = self.cleaned_data["email"]
#         if commit:
#             user.save()
#         return user


class RegistrationForm(UserCreationForm):
    # phone_regex = RegexValidator(regex=r'^\d{9,15}$')
    email = forms.EmailField()
    # phone_no = forms.CharField( max_length=10)
    firstName = forms.CharField(max_length=20)
    lastName = forms.CharField(max_length=20)

    class meta:
        model = User
        field = "__all__"


#
class UpdateProfileForm(forms.ModelForm):
    imag = forms.ImageField(widget=forms.FileInput())

    class Meta:
        model = Profile
        fields = ["imag",]
